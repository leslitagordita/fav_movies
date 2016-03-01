#!/usr/bin/env python
#coding: utf8

import fresh_tomatoes
import media

def main():
	#instances of class Movie
	irma_vep = media.Movie("Irma Vep", "Washed-up French director René Vidal Jean-Pierre Léaud", "images/irma.jpg", 
		"https://www.youtube.com/watch?v=UtY0OBL6Tgo")

	collectionneuse = media.Movie("La Collectionneuse", "A young man (Patrick Bauchau) tells himself high ideals are what kept him from sleeping with a temptress (Haydee Politoff) staying at the same St. Tropez boarding house.",
		"images/collectionneuse.jpg", "https://www.youtube.com/watch?v=HMcPo-S1v-k")

	cocagne = media.Movie("Pays de Cocagne", "Documentery film about the state of French society after the events of May 1968", 
		"images/cocagne.jpg", "https://www.youtube.com/watch?v=eP8nEqZu3gI")

	velvet = media.Movie("Blue Velvet", "College student Jeffrey Beaumont encounters a series of bizarre events in his hometown", 
		"images/velvet.jpg", "https://www.youtube.com/watch?v=5nz1x_XYU0I")

	paris = media.Movie("Paris, Texas","A disheveled man who wanders out of the desert, Travis Henderson (Harry Dean Stanton) seems to have no idea who he is. Soon Travis must confront his wife, Jane (Nastassja Kinski), and try to put his life back together.", 
		"images/paris.jpg","https://www.youtube.com/watch?v=9e590FeeGCM")

	atame = media.Movie("Atame!", "Newly released from a mental institution, Ricky (Antonio Banderas) heads straight for a reunion with the love of his life, B-movie actress Marina (Victoria Abril).",
		"images/atame.jpg", "https://www.youtube.com/watch?v=mHm9qqrl_Uc")



	#array of movies
	movies = [irma_vep, collectionneuse, cocagne, velvet, paris, atame]

	#calling open_movies_page method and passing array of movies with Movie instances
	fresh_tomatoes.open_movies_page(movies)

	print(media.Movie.__doc__)

if __name__ == '__main__':
    main()




    