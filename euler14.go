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

const(
	START=999999;
)

func main(){
	s := uint(1);

	fmt.Printf("Project Euler Problem 14\n");

	s=START;
	for {
		s=next(s);
		s--;
		//fmt.Printf("The next number in the sequence isi %d\n", s);
		//if s==1{break;}
	}

	fmt.Printf("The number that produces the longest chain which is under one million is %d\n", s);
}

func next(in uint)(ret uint){
		if in%2==0{	/* if even */
			ret = in/2;
		}
		else { /* if odd */
			ret = 3*in+1;
		}
	return ret;
}

