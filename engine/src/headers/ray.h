#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "objects.h"

#ifndef RAY_H
#define RAY_H

/**
 * @brief
 * Shoot ray to trace racing.
 * It will be one pixel of the screen.
 *
 * @param screen_pos Position of rendered pixel.
 * @param camera_pos Position of camera.
 * @param camera_dir Direction vectors of camera.
 * First is forward (its length is distance of screen).
 * Second is sideways and third is up aor down.
 * @param lights Array of lights.
 * Every light is LIGHT_SIZE times integer.
 * \n
 * 0-2: position of light (x,y,z)
 * \n
 * 4: color of light (null,r,g,b)
 * @param lights_count Count of lights.
 * @param triangles Array of triangles.
 * Every triangle is TRIANGLE_SIZE times integer.
 * Triangles are relative to center of Cartesian system.
 * \n
 * 0-2: vertex 1 (x,y,z)
 * \n
 * 3-5: vertex 2 (x,y,z)
 * \n
 * 6-8: vertex 3 (x,y,z)
 * \n
 * 9: color of vertex 1 (null,r,g,b)
 * \n
 * 10: color of vertex 2 (null,r,g,b)
 * \n
 * 11: color of vertex 3 (null,r,g,b)
 * @param triangles_count Count of triangles.
 */
int32_t shoot(num_type screen_pos[2],
            num_type camera_pos[3],
            num_type camera_dir[CAMERA_SIZE],
            num_type *lights, int lights_count,
            num_type *triangles, int triangles_count);

int find_triangle(
    num_type dir_vector[N],
    num_type camera_pos[N],
    num_type *triangles, int triangles_count);

void add_vectors3(num_type out[N], num_type vec1[N], num_type vec2[N]);
void sub_vectors3(num_type out[N], num_type vec1[N], num_type vec2[N]);
void scale_vector3(num_type out[N], num_type vec1[N], num_type scale);

num_type dot(num_type vec1[N], num_type vec2[N]);

num_type vector_length(num_type vector[N]);
num_type point_orientation(num_type a[N], num_type b[N], num_type p[N]);

void mult_matrix(num_type out[N], num_type mat[N][N], num_type vec[N]);
int invert_matrix(num_type inverse[N][N], num_type input[N][N]);

void print_matrix(num_type matrix[N][N]);
void print_vectorN(num_type *vector);
void print_vector(num_type *vector, int length);

#endif