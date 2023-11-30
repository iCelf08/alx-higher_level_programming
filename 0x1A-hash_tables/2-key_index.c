0-hash_table_create.c
#include "hash_tables.h"
/**
 * key_index - Gets  the index at which a key:value
 *      pair stored in array of the hash table.
 * @key: The key to get the index of.
 * @size: size of array of the hash table
 *
 * Return: The index of the key
 * Description: use the djb2 algo
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
return (hash_djb2(key) % size);
}
