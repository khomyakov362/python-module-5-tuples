# task 1

lit_genres = ('Novel', 'Novella', 'Fantasy', 'Sci-Fi')
numbers = (3, 7, 9, 1, 6, 8, 2, 5, 4)

print(len(lit_genres))
print(len(numbers))

print(max(lit_genres))
print(max(numbers))

print(min(lit_genres))
print(min(numbers))

print(sum(numbers))

sorted_genres_non_reverse = tuple(sorted(lit_genres))
sorted_genres_reverse = tuple(sorted(lit_genres, reverse=True))
sorted_numbers_non_reverse = tuple(sorted(numbers))
sorted_numbers_revers= tuple(sorted(numbers, reverse=True))


print(sorted_genres_non_reverse)
print(sorted_genres_reverse)
print(sorted_numbers_non_reverse)
print(sorted_numbers_revers)

# task 2

cinema_genres = ("Комедия", "Экшн", "Пеплум", "Триллер")
genres_list = list(cinema_genres)
genres_list.insert(2, "Фэнтези")
updated_genres = tuple(map(lambda st: st.replace("Экшн", "Боевик"), genres_list))
print(updated_genres)
genres_string = "Обновлённые жанры кино: " + ', '.join(updated_genres)
print(genres_string)

# task 3

desert_island_set_1 = {
      'eBook' 
    , 'fishing rod'
    , 'first aid kit'
    , 'compass'
    , 'map'
    , 'torh'
    , 'Desert Island Survival Guide'
    , 'knife'
    , 'axe'
    , 'shovel'
}

desert_island_set_2 = {
      'mp3 player' 
    , 'radio'
    , 'first aid kit'
    , 'compass'
    , 'spare batteries'
    , 'torh'
    , 'survival rations'
    , 'knife'
    , 'axe'
    , 'handsaw'
}

taken_by_both = desert_island_set_1.union(desert_island_set_2)
taken_by_me = desert_island_set_1.difference(desert_island_set_2)
taken_by_them = desert_island_set_2.difference(desert_island_set_1)
taken_by_both_at_once = desert_island_set_1.intersection(desert_island_set_2)

print(taken_by_both)
print(taken_by_me)
print(taken_by_them)
print(taken_by_both_at_once)

# task 4

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

genres_set = set(cinema_genres)
genres_set.add("романтическа комедия")
genres_set.add("документальное кино")
genres_set.pop()

cinema_genres_list = list(genres_set)
print(cinema_genres_list)



