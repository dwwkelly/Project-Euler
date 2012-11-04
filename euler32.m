clear all; clc;

l = 1:9;

tmp = perms(l);

products = [];
pSave = [];

for ii = 1 : length(tmp)
    
   n  =  tmp(ii, :);
   
   m1 = n(1) + 10*n(2);
   m2 = n(3) + 10*n(4) + 100*n(5);
   p  = n(6) + 10*n(7) + 100*n(8) + 1000*n(9);
   
   if m1*m2 == p && isempty(find(pSave == p))
       pSave = [pSave p];
       products = [products p];
   end
end


pSave = [];
for ii = 1 : length(tmp)
    
   n  =  tmp(ii, :);
   
   m1 = n(1);
   m2 = n(2) + n(3)*10 + 100*n(4) + 1000*n(5);
   p  = n(6) + 10*n(7) + 100*n(8) + 1000*n(9);
   
   if m1*m2 == p  && isempty(find(pSave == p))
       pSave = [pSave p];
       products = [products p];
   end
end

fprintf('%d\n', sum(products));