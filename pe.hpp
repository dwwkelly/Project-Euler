/*
 * =====================================================================================
 *
 *       Filename:  pe.hpp
 *
 *    Description:  template library for project euler
 *
 *        Version:  1.0
 *        Created:  02/15/2010 10:14:38 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Devin Kelly (), dkelly@wpi.edu
 *        Company:  WPI
 *
 * =====================================================================================
 */

#include <iostream>
template<class T>
T gcd(T a, T b){
	if(b > a)
		swap(&a,&b);
	T m = a%b;	
	T tmp = a;

	do{
		tmp = b;
		b=m;
		m=tmp%b;
	}
	while(m!=0);

	return b;
}

template<class T>
void swap(T* a, T* b){
	T tmp = *a;
	*a=*b;
	*b=tmp;
	return;
}
