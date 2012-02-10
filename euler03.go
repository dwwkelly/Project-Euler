/*
	copyright 2009 Devin Kelly                                                                                                 
	This software is free software; you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation; either version 3, or (at your option)
	any later version.

	This software is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License along
	with this program; if not, write to the Free Software Foundation, Inc.,
	51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
*/

package main

import (
	 "fmt";
	)


const (n = 600851475143;
	nPrimes = 10000;
);

func main(){

	tmp :=bool(true);
	i := uint64(1);
	j := uint64(10);
	largest :=uint64(0);

	fmt.Printf("Project Euler Problem 3\n");

	for {
		j++;
		tmp = isPrime(j);
		if tmp == true {
			if factor(j,n){
				if j>largest{
					largest=j;
				}
			}
			i++;
			if i >= nPrimes{
				break;
				fmt.Printf("broke\n");
			}
		}
	}

	fmt.Printf("The largest prime factor is: %d\n",largest);
}


func factor(in uint64, n uint64) (ret bool) {
	if n%in == 0{
		ret = true;
	}	
	else {
		ret = false;
	}

	return ret;
}

func isPrime(in uint64) (ret bool){
	tmp := uint64(2);
	
	for tmp=2; tmp<=in; tmp++ {
		if in%tmp == 0{
			break;
		}
	}

	if tmp == in {
		ret = true;
	}
	else {
		ret = false;
	}

	return ret;
}
