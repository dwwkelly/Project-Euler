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

const (
	N = 500;
)

func main(){
	n := uint(1);
	adder := uint(1);

	fmt.Printf("Project Euler Problem 12\n");

	for {
		adder++;
		n=n+adder;
		if nfactors(n) > 500{ break; }
	}

	fmt.Printf("The first triangle number with over 500 divisors is %d\n", n);
}

func nfactors(in uint)(ret uint){
	i := uint(0);
	ret = uint(0);

	for i=1; i <= uint(math.Sqrt(float64(in))+1) ; i++ {
	// this is the trick... it's a little awkward in GO
		if in%i==0 {
			ret+=2;
		}
	}
	return ret;
}

