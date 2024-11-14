#include <stdint.h>

#define TRIANGLE_SIZE 12
#define LIGHT_SIZE 4

typedef struct
{
    int x, y;
} Vector2;

typedef struct
{
    int x, y, z;
} Vector3;

/**
 * @brief
 * Shoot ray to trace racing.
 *
 * @param screen_pos
 * @param camera_pos
 * @param camera_dir
 * @param lights
 * @param lights_count Array of lights.
 * Every light is LIGHT_SIZE times integer.
 * \n
 * 0-2: position of light (x,y,z)
 * \n
 * 4: color of light (null,r,g,b)
 * @param triangles Array of triangles.
 * Every triangle is TRIANGLE_SIZE times integer.
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
 * @param triangles_count Count of triangles as objects,
 * not count of integers in triangles.
 */
void shoot(Vector2 screen_pos,
           Vector3 camera_pos,
           Vector3 camera_dir,
           int32_t *lights, int lights_count,
           int32_t *triangles, int triangles_count)
{
}

int echo()
{
    return sizeof(int);
}