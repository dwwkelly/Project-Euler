clear all;
close all;
clc;

load fibo.txt

if 0
    prev = fibo(2,:);

    for ii=3:length(fibo)
       current = fibo(ii,:);
       if current(2) ~= prev(2)
          fprintf('%i\n', current(1)-prev(1))
          prev    = fibo(ii,:);
       end

    end
else
    adds = [4 5 5 5 4 5 5 5 5 4 5 5 5 5];

    digits=3;
    n=11;
    while 1
        for ii=1:length(adds)
           n = n+adds(ii);
           digits=digits+1;
           if digits >= 1000
               fprintf('n: %d, digits: %d\n', n, digits);
               return;
           end
        end
    end
end