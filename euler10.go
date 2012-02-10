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
	"math";
	)


const(
	n = 2000000;
);

func main(){

	i := uint64(1);
	j := uint64(1);
	sum :=uint64(0);
	tmp := uint64(0);
	limit1 := uint64(math.Ceil(math.Sqrt(float64(n))));
	limit2 := uint64(0);

	var primes [n+1]uint;

	fmt.Printf("Project Euler Problem 10\n");

	/* sieve of Eratosthenes initialization */
	primes[0]=0;
	primes[1]=0;
	for i=2;i<n;i++ {
		primes[i] = 1;
	}

	/* doing the sieving */
	/* if you want to reimplement this algorithm... watch out for off-by-one errors */
	for i=2; i<=limit1; i++ {
		if isPrime(i){
			limit2 = uint64(math.Floor((float64(n)/float64(i))));

			for j=2; j <= limit2; j++ {
				tmp = i*j;
				primes[tmp]=0;
			}

		}
	}

	for i=0;i<n;i++ {
		if primes[i]==1{
			sum += i;
		}
	}

	fmt.Printf("The sum of all primes less than 2 million is: %d\n",sum);
}

func isPrime(in uint64) (ret bool){
	tmp := uint64(1);

	if in == 2{
		return true;
	}
	if in < 2 || in%2 == 0{
		return false;
	}

	for tmp=3; tmp<=in; tmp++ {
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
