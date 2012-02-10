clear all;
close all;
clc;

start = [0 1 2];
answer = zeros(1, length(start));
working = start;
lf = 1;
n=lf;

f=factorial(length(start));

for ii=1:length(start)-1
    tmp = linspace(0, (length(working)-1)*f, length(working));
    for kk=1:length(working)
        if tmp(kk) > n
            answer(ii) = working(kk);
            n = n - working(kk-1);
            working(find(working==working(kk))) = [];
            break
        end
    end
end

answer(end) = working;