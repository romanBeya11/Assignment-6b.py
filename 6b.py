import ui
import time

from numpy import random

# Creating an array that holds every card in a standard deck of 52, without JOKERS
deck_of_cards = ['card:ClubsA', 'card:Clubs2', 'card:Clubs3', 'card:Clubs4', 'card:Clubs5', 'card:Clubs6', 'card:Clubs7', 'card:Clubs8', 'card:Clubs9', 'card:Clubs10', 'card:ClubsJ', 'card:ClubsK', 'card:ClubsQ', 'card:SpadesA', 'card:Spades2', 'card:Spades3', 'card:Spades4', 'card:Spades5', 'card:Spades6', 'card:Spades7', 'card:Spades8', 'card:Spades9', 'card:Spades10', 'card:SpadesJ', 'card:SpadesK', 'card:SpadesQ', 'card:HeartsA', 'card:Hearts2', 'card:Hearts3', 'card:Hearts4', 'card:Hearts5', 'card:Hearts6', 'card:Hearts7', 'card:Hearts8', 'card:Hearts9', 'card:Hearts10', 'card:HeartsJ', 'card:HeartsK', 'card:HeartsQ', 'card:DiamondsA', 'card:Diamonds2', 'card:Diamonds3', 'card:Diamonds4', 'card:Diamonds5', 'card:Diamonds6', 'card:Diamonds7', 'card:Diamonds8', 'card:Diamonds9', 'card:Diamonds10', 'card:DiamondsJ', 'card:DiamondsK', 'card:DiamondsQ']

# GLOBAL variables
# Once a card is randomly selected, it is discarded so that it is not used twice
card_1 = random.choice(deck_of_cards)
player_first_card = deck_of_cards.index(card_1)
deck_of_cards.remove(card_1)

card_2 = random.choice(deck_of_cards)
player_second_card = deck_of_cards.index(card_2)
deck_of_cards.remove(card_2)

# These are optional cards, thus their value should be 0 until a user requests the card. In which case, a random card will be selected
card_3 = random.choice(deck_of_cards)
player_third_card = deck_of_cards.index(card_3)
deck_of_cards.remove(card_3)

card_4 = random.choice(deck_of_cards)
player_fourth_card = deck_of_cards.index(card_4)
deck_of_cards.remove(card_4)

card_5 = random.choice(deck_of_cards)
player_fifth_card = deck_of_cards.index(card_5)
deck_of_cards.remove(card_5)

dealer_card_1 = random.choice(deck_of_cards)
dealer_first_card = deck_of_cards.index(dealer_card_1)
deck_of_cards.remove(dealer_card_1)

dealer_card_2 = random.choice(deck_of_cards)
dealer_second_card = deck_of_cards.index(dealer_card_2)
deck_of_cards.remove(dealer_card_2)

player_card_sum = 0
dealer_card_sum = 0
draw_new_card = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
d1 = 0
d2 = 0

# Set their starting amount of virtual coins to $5000
current_profits = 5000

def disable_buttons():
	# Once the program has run, disable certain buttons to control the flow of the game
	view['draw_another_card_button'].enabled = False
	view['draw_another_card_button'].alpha = 0.25
	view['check_cards_button'].enabled = False
	view['check_cards_button'].alpha = 0.25
	
def enable_buttons():
	# Enable buttons to be accessible by the user
	view['draw_another_card_button'].enabled = True
	view['draw_another_card_button'].alpha = 1
	view['check_cards_button'].enabled = True
	view['check_cards_button'].alpha = 1
	
def show_coin_sprite():
	# Animate coin sprites
	number_of_loops = 0
	counter = 0
	while(counter < 4):
		if counter == 1:
			view['imageview8'].image = ui.Image.named('plf:Item_CoinBronze')
			time.sleep(1)
			view['imageview8'].image = ui.Image.named('')
		if counter == 1:
			view['imageview6'].image = ui.Image.named('plf:Item_CoinSilver')
			time.sleep(1)
			view['imageview6'].image = ui.Image.named('')
		if counter == 1:
			view['imageview7'].image = ui.Image.named('plf:Item_CoinGold')
			time.sleep(1)
			view['imageview7'].image = ui.Image.named('')
		counter = counter + 1
		if counter == 3:
			counter = 1
			number_of_loops = number_of_loops + 1
			if number_of_loops == 5:
				view['imageview8'].image = ui.Image.named('plf:Item_CoinGold')
				break
def view_cards_touch_up_inside(sender):
	# View the players cards when the event is handled
	global card_1
	global card_2
	
	# Display their random card
	view['imageview1'].image = ui.Image.named(card_1)
	view['imageview2'].image = ui.Image.named(card_2)
	
	# Disable this button if it is pressed to handle control flow
	view['view_cards_button'].enabled = False
	view['view_cards_button'].alpha = 0.25
	
	# Enable certain cards to help with data flow and control of game
	enable_buttons()

def draw_another_card_touch_up_inside(sender):
	global card_3
	global card_4
	global card_5
	global draw_new_card
	
	# Access this global variable that will enable drawing at most 3 extra cards
	draw_new_card = draw_new_card + 1
	
	if draw_new_card == 1:
		view['imageview3'].image = ui.Image.named(card_3)
		
	elif draw_new_card == 2:
		view['imageview4'].image = ui.Image.named(card_4)
		
	elif draw_new_card == 3:
		view['imageview5'].image = ui.Image.named(card_5)
		
		# Disable this button if it is pressed
		view['draw_another_card_button'].enabled = False
		view['draw_another_card_button'].alpha = 0.25
	
@ui.in_background		
def check_cards_touch_up_inside(sender):
	global player_first_card
	global player_second_card
	global player_third_card
	global player_fourth_card
	global player_fifth_card
	global dealer_first_card
	global dealer_second_card
	global player_card_sum
	global dealer_card_sum
	global p1
	global p2
	global p3
	global p4
	global p5
	global d1
	global d2
	# Display the dealer cards
	view['dealer_card_1_imageview'].image = ui.Image.named(dealer_card_1)
	view['dealer_card_2_imageview'].image = ui.Image.named(dealer_card_2)
	
	# If the draw card button is disable, this implies that it has been pressed three times
	if view['draw_another_card_button'].enabled == False:
		for ace in range(0, 52, 14):
			if player_first_card == ace:
				p1 = 1
			if player_second_card == ace:
				p2 = 1
			if player_third_card == ace:
				p3 = 1
			if player_fourth_card == ace:
				p4 = 1
			if player_fifth_card == ace:
				p5 = 1
			if dealer_first_card == ace:
				d1 = 1
			if dealer_second_card == ace:
				d2 = 1
			
		for twos in range(1, 52, 14):
			if player_first_card == twos:
				p1 = 2
			if player_second_card == twos:
				p2 = 2
			if player_third_card == twos:
				p3 = 2
			if player_fourth_card == twos:
				p4 = 2
			if player_fifth_card == twos:
				p5 = 2
			if dealer_first_card == twos:
				d1 = 2
			if dealer_second_card == twos:
				d2 = 2
				
		for threes in range(2, 52, 14):
			if player_first_card == threes:
				p1 = 3
			if player_second_card == threes:
				p2 = 3
			if player_third_card == threes:
				p3 = 3
			if player_fourth_card == threes:
				p4 = 3
			if player_fifth_card == threes:
				p5 = 3
			if dealer_first_card == threes:
				d1 = 3
			if dealer_second_card == threes:
				d2 = 3
				
		for fours in range(3, 52, 14):
			if player_first_card == fours:
				p1 = 4
			if player_second_card == fours:
				p2 = 4
			if player_third_card == fours:
				p3 = 4
			if player_fourth_card == fours:
				p4 = 4
			if player_fifth_card == fours:
				p5 = 4
			if dealer_first_card == fours:
				d1 = 4
			if dealer_second_card == fours:
				d2 = 4
				
		for fives in range(4, 52, 14):
			if player_first_card == fives:
				p1 = 5
			if player_second_card == fives:
				p2 = 5
			if player_third_card == fives:
				p3 = 5
			if player_fourth_card == fives:
				p4 = 5
			if player_fifth_card == fives:
				p5 = 5
			if dealer_first_card == fives:
				d1 = 5
			if dealer_second_card == fives:
				d2 = 5
				
		for sixes in range(5, 52, 14):
			if player_first_card == sixes:
				p1 = 6
			if player_second_card == sixes:
				p2 = 6
			if player_third_card == sixes:
				p3 = 6
			if player_fourth_card == sixes:
				p4 = 6
			if player_fifth_card == sixes:
				p5 = 6
			if dealer_first_card == sixes:
				d1 = 6
			if dealer_second_card == sixes:
				d2 = 6
				
		for sevens in range(6, 52, 14):
			if player_first_card == sevens:
				p1 = 7
			if player_second_card == sevens:
				p2 = 7
			if player_third_card == sevens:
				p3 = 7
			if player_fourth_card == sevens:
				p4 = 7
			if player_fifth_card == sevens:
				p5 = 7
			if dealer_first_card == sevens:
				d1 = 7
			if dealer_second_card == sevens:
				d2 = 7
				
		for eights in range(7, 52, 14):
			if player_first_card == eights:
				p1 = 8
			if player_second_card == eights:
				p2 = 8
			if player_third_card == eights:
				p3 = 8
			if player_fourth_card == eights:
				p4 = 8
			if player_fifth_card == eights:
				p5 = 8
			if dealer_first_card == eights:
				d1 = 8
			if dealer_second_card == eights:
				d2 = 8
				
		for nines in range(8, 52, 14):
			if player_first_card == nines:
				p1 = 9
			if player_second_card == nines:
				p2 = 9
			if player_third_card == nines:
				p3 = 9
			if player_fourth_card == nines:
				p4 = 9
			if player_fifth_card == nines:
				p5 = 9
			if dealer_first_card == nines:
				d1 = 9
			if dealer_second_card == nines:
				d2 = 9
				
		for tens in range(9, 52, 14):
			if player_first_card == tens:
				p1 = 10
			if player_second_card == tens:
				p2 = 10
			if player_third_card == tens:
				p3 = 10
			if player_fourth_card == tens:
				p4 = 10
			if player_fifth_card == tens:
				p5 = 10
			if dealer_first_card == tens:
				d1 = 10
			if dealer_second_card == tens:
				d2 = 10
				
		for jacks in range(10, 52, 14):
			if player_first_card == jacks:
				p1 = 10
			if player_second_card == jacks:
				p2 = 10
			if player_third_card == jacks:
				p3 = 10
			if player_fourth_card == jacks:
				p4 = 10
			if player_fifth_card == jacks:
				p5 = 10
			if dealer_first_card == jacks:
				d1 = 10
			if dealer_second_card == jacks:
				d2 = 10
				
		for kings in range(11, 52, 14):
			if player_first_card == kings:
				p1 = 10
			if player_second_card == kings:
				p2 = 10
			if player_third_card == kings:
				p3 = 10
			if player_fourth_card == kings:
				p4 = 10
			if player_fifth_card == kings:
				p5 = 10
			if dealer_first_card == kings:
				d1 = 10
			if dealer_second_card == kings:
				d2 = 10
				
		for queens in range(12, 52, 14):
			if player_first_card == queens:
				p1 = 10
			if player_second_card == queens:
				p2 = 10
			if player_third_card == queens:
				p3 = 10
			if player_fourth_card == queens:
				p4 = 10
			if player_fifth_card == queens:
				p5 = 10
			if dealer_first_card == queens:
				d1 = 10
			if dealer_second_card == queens:
				d2 = 10
		# Adding all 5 of the players card
		player_card_sum = p1 + p2 + p3 + p4 + p5
		
		# Summing the dealers cards
		dealer_card_sum = d1 + d2
		
		# Comparing both sums to determine the winner
		if dealer_card_sum >= player_card_sum and dealer_card_sum <= 21:
			# In this case the dealer wins
			view['check_cards_label'].text = 'The sum of your cards is: {0}\nThe sum of the dealers cards is: {1}\nThe dealer wins!'.format(player_card_sum, dealer_card_sum)
		else:
			if player_card_sum <= 21:
				# The player wins in this permutation
				view['check_cards_label'].text = 'The sum of your cards is: {0}\nThe sum of the dealers cards is: {1}\nYou win!'.format(player_card_sum, dealer_card_sum)
				
				# In this case, increase the profits by $2000
				for increase_profits in range(current_profits, current_profits + 2001, 1):
					time.sleep(0.0001)
					view['betting_label'].text = '$' + str(increase_profits)
				show_coin_sprite()
	else:
		# Meaning that they have NOT selected selected another card
		for ace in range(0, 52, 14):
			if player_first_card == ace:
				p1 = 1
			if player_second_card == ace:
				p2 = 1
			if dealer_first_card == ace:
				d1 = 1
			if dealer_second_card == ace:
				d2 = 1
			
		for twos in range(1, 52, 14):
			if player_first_card == twos:
				p1 = 2
			if player_second_card == twos:
				p2 = 2
			if dealer_first_card == twos:
				d1 = 2
			if dealer_second_card == twos:
				d2 = 2
				
		for threes in range(2, 52, 14):
			if player_first_card == threes:
				p1 = 3
			if player_second_card == threes:
				p2 = 3
			if dealer_first_card == threes:
				d1 = 3
			if dealer_second_card == threes:
				d2 = 3
				
		for fours in range(3, 52, 14):
			if player_first_card == fours:
				p1 = 4
			if player_second_card == fours:
				p2 = 4
			if dealer_first_card == fours:
				d1 = 4
			if dealer_second_card == fours:
				d2 = 4
				
		for fives in range(4, 52, 14):
			if player_first_card == fives:
				p1 = 5
			if player_second_card == fives:
				p2 = 5
			if dealer_first_card == fives:
				d1 = 5
			if dealer_second_card == fives:
				d2 = 5
				
		for sixes in range(5, 52, 14):
			if player_first_card == sixes:
				p1 = 6
			if player_second_card == sixes:
				p2 = 6
			if dealer_first_card == sixes:
				d1 = 6
			if dealer_second_card == sixes:
				d2 = 6
				
		for sevens in range(6, 52, 14):
			if player_first_card == sevens:
				p1 = 7
			if player_second_card == sevens:
				p2 = 7
			if dealer_first_card == sevens:
				d1 = 7
			if dealer_second_card == sevens:
				d2 = 7
				
		for eights in range(7, 52, 14):
			if player_first_card == eights:
				p1 = 8
			if player_second_card == eights:
				p2 = 8
			if dealer_first_card == eights:
				d1 = 8
			if dealer_second_card == eights:
				d2 = 8
				
		for nines in range(8, 52, 14):
			if player_first_card == nines:
				p1 = 9
			if player_second_card == nines:
				p2 = 9
			if dealer_first_card == nines:
				d1 = 9
			if dealer_second_card == nines:
				d2 = 9
				
		for tens in range(9, 52, 14):
			if player_first_card == tens:
				p1 = 10
			if player_second_card == tens:
				p2 = 10
			if dealer_first_card == tens:
				d1 = 10
			if dealer_second_card == tens:
				d2 = 10
				
		for jacks in range(10, 52, 14):
			if player_first_card == jacks:
				p1 = 10
			if player_second_card == jacks:
				p2 = 10
			if dealer_first_card == jacks:
				d1 = 10
			if dealer_second_card == jacks:
				d2 = 10
				
		for kings in range(11, 52, 14):
			if player_first_card == kings:
				p1 = 10
			if player_second_card == kings:
				p2 = 10
			if dealer_first_card == kings:
				d1 = 10
			if dealer_second_card == kings:
				d2 = 10
				
		for queens in range(12, 52, 14):
			if player_first_card == queens:
				p1 = 10
			elif player_second_card == queens:
				p2 = 10
			elif dealer_first_card == queens:
				d1 = 10
			elif dealer_second_card == queens:
				d2 = 10
		# Adding both of the players card
		player_card_sum = p1 + p2
		
		# Summing the dealers cards
		dealer_card_sum = d1 + d2
		
		# Comparing both sums to determine the winner
		if dealer_card_sum >= player_card_sum and dealer_card_sum <= 21:
			# In this case the dealer wins
			view['check_cards_label'].text = 'The sum of your cards is: {0}\nThe sum of the dealers cards is: {1}\nThe dealer wins!'.format(player_card_sum, dealer_card_sum)
		else:
			if player_card_sum <= 21:
				# The player wins in this permutation
				view['check_cards_label'].text = 'The sum of your cards is: {0}\nThe sum of the dealers cards is: {1}\nYou win!'.format(player_card_sum, dealer_card_sum)
				
				# In this case, increase the profits by $2000
				for increase_profits in range(current_profits, current_profits + 2001, 1):
					time.sleep(0.001)
					view['betting_label'].text = '$' + str(increase_profits)				
				show_coin_sprite()
				
view = ui.load_view()
view.present('full_screen')
disable_buttons()
# Diaplay gold coin sprite
view['imageview8'].image = ui.Image.named('plf:Item_CoinGold')
