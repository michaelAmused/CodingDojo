class MathDojo
    def initialize
        @total = 0
    end
    def add *args
        args.flatten!
        args.each {|i| @total += i}
        self
    end
    def subtract *args
        args.flatten!
        args.each {|i| @total -= i}
        self
    end
    def result
        puts @total
    end
end

challenge1 = MathDojo.new.add(2).add(2,5).subtract(3 ,2).result
challenge2 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2, 3], [1.1, 2.3]).result
