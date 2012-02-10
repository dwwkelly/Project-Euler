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

#include <string>
#include <iostream>
#include <sstream>

bool isPalindrome(int n);

int main(int argc, char** argv){
	int i,j;
	int largest = 0;

	for(i=999;i>100;i--){
		for(j=i;j>100;j--)
			if(isPalindrome(i*j) && i*j > largest){
					largest = i*j;
				}

	}

	std::cout << "the palindrome is: " << largest << "\n";

	return 0;

}


bool isPalindrome(int n){
	std::string s;
	std::stringstream tmp;
	int i = 0;

	tmp << n;
	s = tmp.str();

	if(s.length()%2) /* if the string is odd length, remove the middle character */
		s.erase((s.length()-1)/2,1);

	for(i=0; i < (s.length()/2); i++) {
		if( s[i] != s[s.length()-1-i] ) {
			break;
		}
	}
	
	if (i==s.length()/2)
		return true;
	else 
		return false;
}

