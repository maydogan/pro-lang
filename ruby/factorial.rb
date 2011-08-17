#!/usr/bin/ruby
def fac(i)
  if i == 0
    1
  else
    i * fac(i - 1)
  end
end
puts fac(5)
