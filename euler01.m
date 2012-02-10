% copyright 2009 Devin Kelly                                                                                                 
%
% This is free software; you can redistribute it and/or modify
% it under the terms of the GNU General Public License as published by
% the Free Software Foundation; either version 3, or (at your option)
% any later version.
%
% This software is distributed in the hope that it will be useful,
% but WITHOUT ANY WARRANTY; without even the implied warranty of
% MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
% GNU General Public License for more details.
%
% You should have received a copy of the GNU General Public License along
% with this program; if not, write to the Free Software Foundation, Inc.,
% 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


function [s] = euler01() %#eml

    limit = 10e6;
    nums = zeros(limit,1);
    k=0;
    
    for k=1:limit-1
        if ~mod(k,5) || ~mod(k,3)
            nums(k)=k;
        end
    end
    
    s = sum(nums);
    
end
