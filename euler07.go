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

func main(){

	i := uint(0);
	j := uint(0);

	fmt.Printf("Project Euler Problem 7\n");

	for {
		i++;
		if isPrime(i){
			j++;
		}
		if j==10001{
			break;
		}

	}

	fmt.Printf("The 1001st prime is: %d\n",i);
}

func isPrime(in uint) (ret bool){
	tmp := uint(2);

	if in == 0{
		return false;
	}
	if in == 1{
		return false;
	}

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
