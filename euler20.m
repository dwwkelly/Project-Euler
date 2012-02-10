clc; clear all; 

numbers = zeros(1,25);

for ii=1:25
    numbers(ii) = sum(num2str(factorial(ii))*1-'0');
end

disp(reshape(numbers,5,5))