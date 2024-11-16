#include <stdint.h>

#include "headers/ray.h"

int32_t shoot(num_type screen_pos[2],
              num_type camera_pos[N],
              num_type camera_dir[CAMERA_SIZE],
              num_type *lights, int lights_count,
              num_type *triangles, int triangles_count)
{
    // vector of ray direction
    num_type dir_vector[N];
    // scaled vectors of camera direction (1,2)
    num_type scaled_side_camera[N], scaled_up_camera[N];

    scale_vector3(scaled_side_camera, &camera_dir[N], screen_pos[0]);
    scale_vector3(scaled_up_camera, &camera_dir[N * 2], screen_pos[1]);

    add_vectors3(dir_vector, scaled_side_camera, scaled_up_camera);
    add_vectors3(dir_vector, dir_vector, &camera_dir[0]);

    /*printf("cam_dir: ");
    print_vectorN(&camera_dir[0]);
    printf("dir_vec: ");
    print_vectorN(dir_vector);
    printf("\n");*/

    num_type inverse[N][N];
    invert_matrix((num_type(*)[N]) & triangles[0], inverse);

    // print_matrix(inverse);
    int found_trian_index = find_triangle(dir_vector, camera_pos, triangles, triangles_count);
    if (found_trian_index < 0)
        return -1; // no triangle colides - return black
    // printf("Found\n");

    num_type(*triangle)[N] = (num_type(*)[N]) & triangles[found_trian_index * TRIANGLE_SIZE];

    // print_matrix(triangle);
    // print_vectorN(triangle[N]);
    return triangle[N][0];
}

int find_triangle(
    num_type dir_vector[N],
    num_type camera_pos[N],
    num_type *triangles, int triangles_count)
{
    int index = -1;
    num_type closest_distance = -1;
    for (int i = 0; i < triangles_count; i++)
    {
        /**
         * @brief
         * @param b part of eq
         * @param v,w dir vector of plane
         * @param x parameters of eqs (t, s, q)
         * @param A triangle
         * @param i_A inverse A
         */
        num_type b[N], v[N], w[N], x[N];
        num_type A[N][N], i_A[N][N];
        num_type(*triangle)[N] = (num_type(*)[N]) & triangles[i * TRIANGLE_SIZE];

        sub_vectors3(b, triangle[0], camera_pos);
        sub_vectors3(v, triangle[1], triangle[0]);
        sub_vectors3(w, triangle[2], triangle[0]);

        // printf("triangle:");
        // print_matrix(triangle);

        for (int o = 0; o < N; o++)
        {
            A[o][0] = dir_vector[o];
            A[o][1] = -1 * v[o];
            A[o][2] = -1 * w[o];
        }

        // printf("A:");
        // print_matrix(A);

        if (invert_matrix(i_A, A))
            continue; // matice je regularni
        // nalezeni parametru rovnic primky a roviny
        mult_matrix(x, i_A, b);

        /**
         * @param intersection intersection of line and plane
         * @param scaled_dir scaled ray direction of line parameter t
         */
        num_type intersection[N], scaled_dir[N];
        num_type t = x[0];

        scale_vector3(scaled_dir, dir_vector, t);
        add_vectors3(intersection, camera_pos, scaled_dir);

        /*print_vectorN(scaled_dir);
        print_vectorN(intersection);
        print_matrix(triangle);*/

        num_type o1 = point_orientation(triangle[0], triangle[1], intersection);
        num_type o2 = point_orientation(triangle[1], triangle[2], intersection);
        num_type o3 = point_orientation(triangle[2], triangle[0], intersection);
        //printf("%f %f %f\n", o1, o2, o3);

        if (!(
                (o1 >= 0 && o2 >= 0 && o3 >= 0) ||
                (o1 <= 0 && o2 <= 0 && o3 <= 0)))
            continue; // intersection is not inside triangle

        num_type cam_inter_vector[N];

        sub_vectors3(cam_inter_vector, camera_pos, intersection);
        // print_vectorN(cam_inter_vector);
        num_type cam_distance = vector_length(cam_inter_vector);
        // printf("%f\n", cam_distance);
        if (closest_distance < 0 ||
            closest_distance > cam_distance)
        {
            index = i;
            closest_distance = cam_distance;
        }
    }
    // no triangle on ray
    // printf("Closes distance: %f\n", closest_distance);
    return index;
}

void add_vectors3(num_type out[N], num_type vec1[N], num_type vec2[N])
{
    for (int i = 0; i < N; i++)
        out[i] = vec1[i] + vec2[i];
}

void sub_vectors3(num_type out[N], num_type vec1[N], num_type vec2[N])
{
    for (int i = 0; i < N; i++)
        out[i] = vec1[i] - vec2[i];
}

void scale_vector3(num_type out[N], num_type vec1[N], num_type scale)
{
    for (int i = 0; i < N; i++)
        out[i] = vec1[i] * scale;
}

num_type dot(num_type vec1[N], num_type vec2[N])
{
    return (
        (vec1[0] * vec2[0]) +
        (vec1[1] * vec2[1]) +
        (vec1[2] * vec2[2]));
}

num_type vector_length(num_type vector[N])
{
    num_type sum = 0;
    for (int i = 0; i < N; i++)
        sum += vector[i] * vector[i];
    return sqrt(sum);
}

num_type point_orientation(num_type a[N], num_type b[N], num_type p[N])
{
    int x = 1;
    int y = 2;
    return ((b[x] - a[x]) * (p[y] - a[y])) - ((b[y] - a[y]) * (p[x] - a[x]));
}

void mult_matrix(num_type out[N], num_type mat[N][N], num_type vec[N])
{
    for (int y = 0; y < N; y++)
    {
        out[y] = 0;
        for (int x = 0; x < N; x++)
            out[y] += mat[y][x] * vec[x];
    }
}

int invert_matrix(num_type inverse[N][N], num_type input[N][N])
{
    num_type temp[N][2 * N]; // Rozšířená matice (input | identity)

    // Inicializace rozšířené matice
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            temp[i][j] = input[i][j];          // Původní matice vlevo
            temp[i][j + N] = (i == j) ? 1 : 0; // Jednotková matice vpravo
        }
    }

    /*print_vector(temp[0], 6);
    print_vector(temp[1], 6);
    print_vector(temp[2], 6);*/

    // Gauss-Jordanova eliminace
    for (int i = 0; i < N; i++)
    {
        // Najít pivot
        num_type pivot = temp[i][i];
        if (fabs(pivot) < EPSILON)
        {
            // Matice není regulární (determinant je nulový)
            return 1;
        }

        // Normalizovat řádek na pivot = 1
        for (int j = 0; j < 2 * N; j++)
        {
            temp[i][j] /= pivot;
        }

        // Zrušit hodnoty nad a pod pivotem
        for (int k = 0; k < N; k++)
        {
            if (k != i)
            { // Ostatní řádky
                num_type factor = temp[k][i];
                for (int j = 0; j < 2 * N; j++)
                {
                    temp[k][j] -= factor * temp[i][j];
                }
            }
        }
    }

    // Extrahovat inverzní matici z rozšířené matice
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            inverse[i][j] = temp[i][j + N];
        }
    }

    return 0; // Úspěch
}

void print_vectorN(num_type *vector)
{
    print_vector(vector, N);
}

void print_vector(num_type *vector, int length)
{
    for (int i = 0; i < length; i++)
        printf("%f ", vector[i]);
    printf("\n");
}

void print_matrix(num_type matrix[N][N])
{
    printf("\n");
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%f ", matrix[i][j]);
        }
        printf("\n");
    }
}