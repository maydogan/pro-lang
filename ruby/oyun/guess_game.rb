def number_produce()
	number = [1,2,3,4,5,6,7,8,9]
	number.shuffle[0,4].join("")
end

def guess_game()
	num = number_produce()
	step = 10
	puts "10 adimda sayiyi bulman gerek!! Hazirsan rakamlari farkli 4 basamakli sayi gir bakalim:"
	while step > 0 
		guess = gets.strip
		if guess.length == 4  and !guess.match(/\D/) and guess.split("").uniq.length == 4
			if guess == num
				puts " Harika misin ne!!"
				break

			else
				exist = match = 0
				for i in 0..(num.length - 1)
					if guess[i] == num[i]
						match += 1
					elsif num.include? guess[i]
						exist += 1
					end
				end
				puts "%d exist %d match" % [exist,match] #exist var olan sayi, match eslesen sayi
			end

		else
			puts "Kardes dort basamakli ve rakamlari farkli sayi dedik! "
		end
		step -= 1
	end
	puts "Malesef galip gelemedin dostum \nTahmin etmen gereken sayi:", num	
end
puts guess_game()

