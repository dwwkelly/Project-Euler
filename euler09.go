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

const (
	limit = 1000;
	z = 2000;
	x = 1000;
)

func main(){

	a := uint(1);
	b := uint(1);
	c := uint(1);
	product := uint(0);

	fmt.Printf("Project Euler Problem 9\n");

	for a=1;a<1000;a++{
		for b=1;b<1000;b++ {
			if z==(2*a*b+1000000)/(a+b){
				c = 1000 - a - b;
				if a*a+b*b ==c*c {goto Done}
			}
		} 
	}

	Done:
	fmt.Printf("a is: %d b is: %d\n",a,b);
	product = a*b*c;
	fmt.Printf("The product of the pythagorean triple that sums to 1000 is %d\n",product);
}


