#!/usr/bin/ruby
def fib(n)
  fir = 0
  sec = 1
  n.times do |i|
    fir, sec = sec, sec + fir
  end
return fir
end

