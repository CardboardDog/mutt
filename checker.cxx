/*
 * checker.cxx
 *
 * (C) EN 2025 - THIS CODE IS UNDER THE MIT LICENSE
 *
 * created for the mutt programming language
 *
 * this takes the source code and checks it 
 * for common mistakes such as unclosed brackets
 * and other syntax errors.
 */

#include<checker.hxx>

/* check for unclosed brackets */
bool check_brackets(std::string source){
	return true;
}

/* check for improper statements */
bool check_statements(std::string source){
	return true;
}

/* check for incorrectly defined symbols */
bool check_symbols(std::string source){
	return true;
}

/* check for indentation mistakes */
bool check_indents(std::string){
	return true;
}

/* check all three stages of possible mistakes */
bool check_syntax(std::string source){
	return check_brackets(source) &&
		check_symbols(source) &&
		check_indents(source) &&
		check_statements(source);
}
