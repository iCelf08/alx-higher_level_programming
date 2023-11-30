0-hash_table_create.c
#include "hash_tables.h"

/**
 * hash_djb2 - Hash function implementing the djb2 algorithm.
 * @str: The string to hash.
 *
 * Return:calculated hash.
 */
unsigned long int hash_djb2(const unsigned char *str)
{
unsigned long int h;
int c;
h = 5381;
while ((c = *str++))
hash = ((h << 5) + h) + c;
return (h);
}
