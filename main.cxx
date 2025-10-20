/*
 * MUTTC
 *
 * (C) EN 2025 - THIS CODE IS UNDER THE MIT LICENSE
 *
 * created for the mutt programming language
 *
 * this takes a mutt file and converts it into
 * a C source file and a C header.
 * it takes a mutt file as arg1 and the
 * and the resulting C source as arg1
 * arg2 will be the C header.
 * arg3 is optional and is either a c or h
 * depending on what results you want.
 */

#include<fstream>
#include<iostream>
#include<sstream>
#include<vector>
#include<checker.hxx>

int main(int arg_count, char** args){
	/* make sure we have all three arguments */
	if(arg_count >= 4){
		std::cerr << "invalid arguments\n";
		return -1;
	}

	/* store the arguments */
	std::string mutt_in(args[1]);
	std::string c_out  (args[2]);
	std::string h_out  (args[3]);
	char mode = (arg_count == 5)? args[4][0] : 0;

	/* read our mutt source file */
	std::string mutt_source;
	{
		std::ifstream file(mutt_in);
		if(!file.is_open()){
			std::cerr << "failed to open mutt source: " << mutt_in << "\n";
			return 1;
		}

		std::stringstream buffer;
		buffer << file.rdbuf();
		mutt_source = buffer.str();
	}
	
	/* convert triple spaces to tabs */
	mutt_source = force_tabs(mutt_source);

	/* check for syntax errors */
	if(!check_syntax(mutt_source))
		return 2;

	/* transpile the source and header */
	if(!mode || mode == 'c')
		std::string c_header = compile_header(mutt_source);
	if(!mode || mode == 'h')
		std::string c_source = compile_source(mutt_source);
	
	std::cout << mutt_source << std::endl;
}
