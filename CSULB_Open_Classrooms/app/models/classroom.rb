class Classroom < ApplicationRecord

  def initalize(class_name, current_time)
    @name = class_name

    # current_time is in form ex: 3:40AM
    # will be array [currentTime, AM||PM]
    @current_time = splitTimeForComparisons( current_time )
    @class_times = []
  end

  def addClassTimeOccurance(class_time)
    @class_times.append(class_time)
  end

  # does current time match any class time listed in schedule
  def isClassOnNow
    # O(n) to search through all class times, if unsorted
    for class_time in @class_times

      # first break apart class_time, into [start, end, AM||PM]
      class_time_info = splitTimeForComparisons(class_time)

      # check if matching, in terms of before noon or afternoon
      if class_time[2] == @current_time[1]
        if class_time[0] < @current_time[0] && class_time[1] > @current_time[0]
            return true
        end
      end

    end

    return false
  end

  def splitTimeForComparisons(class_time)
    # class_time is in form example: 7:30-8:20PM,
    # so split on (hyphen or letter)

    # returns an array [startTime, endTime, AM||PM]

    # match hyphen(-) or alphanumerical character (letter)
    regex_delimeter_to_split_on = "[-]|\w"
    return class_time.split( regex_delimeter_to_split_on )
  end
end
