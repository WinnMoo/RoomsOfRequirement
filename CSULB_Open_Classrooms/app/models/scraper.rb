require 'HTTParty'
require 'Nokogiri'
require 'open-uri'

#HTML object that we're working with
doc = Nokogiri::HTML(open("http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2017/By_Subject/CECS.html"))

#Create arrays of data that we're working with
@listOfClassrooms = Array.new
@listOfTimes = Array.new

#If the page source has the markup for the beginning of a new row, this will grab all the data from that row
#Even though we have all the data from the row, only specific elements are saved to the array
#Allows for addition of new arrays that holds other kinds of data such as days or class number
doc.css('tr').each do |x|
  	section, type, days, unknown, @time, teacher, @classroom= x.css('td').map(&:content)

  	#If statement to catch elements that have "TBA", otherwise append to the array
	if @classroom != "TBA"
		@listOfClassrooms << @classroom
	end
	#If statement to catch elements that have "TBA", otherwise append to the array
	if @time != "TBA"
		@listOfTimes << @time
	end

end

#For statement to print out the classes and times
(0...@listOfClassrooms.size).each do |index|
  puts "Class: #{@listOfClassrooms[index]} Time: #{@listOfTimes[index]}"
end

#TODO:
#1. Catch elements that have no text ""
#2. Output data into a text file






