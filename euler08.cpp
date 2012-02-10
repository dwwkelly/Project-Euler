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
#include <boost/lexical_cast.hpp>

int main(int argc, char** argv){
	int i,j,tmp2;
	int largest = 0;
	int n[5];

	std::string tmp;

	std::string s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

	for (i = 0;i < s.length()-5;i++){
		tmp = s.substr(i,5);
		for(j=0;j<5;j++){
			n[j]=boost::lexical_cast<int>(tmp[j]);
		}
		tmp2 = n[0]*n[1]*n[2]*n[3]*n[4];
		if (tmp2>largest)
			largest = tmp2;
	}

	std::cout << "the largest is: " << largest << "\n";

	return 0;

}


