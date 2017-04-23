require 'HTTParty'
require 'Nokogiri'
require 'open-uri'

doc = Nokogiri::HTML(open("http://web.csulb.edu/depts/enrollment/registration/class_schedule/Spring_2017/By_Subject/CECS.html"))

@listOfClassrooms = Array.new
@listOfTimes = Array.new

doc.css('tr').each do |x|
  	section, type, days, asdf, @time, teacher, @classroom= x.css('td').map(&:content)

	if @classroom != "TBA"
		@listOfClassrooms << @classroom
	end

	if @time != "TBA"
		@listOfTimes << @time
	end
end


(0...@listOfClassrooms.size).each do |index|
  puts "Class: #{@listOfClassrooms[index]} Time: #{@listOfTimes[index]}"
end








