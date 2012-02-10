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

	i := uint64(1);
	j := uint64(1);

	fmt.Printf("Project Euler Problem 5\n");

	for i=1;i<=20;i++{
		j=lcm(i,j);
	}

	fmt.Printf("The smallest number to be evenly divisable from 1 to 20 is: %d\n",j);
}


func lcm(a uint64, b uint64) (ret uint64) {
	i := uint64(1);
	for i=1;;i++{
		if i%a==0 && i%b==0 {
			break;
		}
	}
	ret = i;
	return ret;
}
