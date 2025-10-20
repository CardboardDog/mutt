/*
 * compiler.hxx
 *
 * (C) EN 2025 - THIS CODE IS UNDER THE MIT LICENSE
 *
 * created for the mutt programming language
 */

#include<iostream>
#include<vector>

#ifndef MUTT_CHECKER_H
#define MUTT_CHECKER_H

struct mutt_compiler{
	unsigned char level = 0;
	bool in_string = false;
	unsigned long cursor = 0;
	std::string mixed_source = "";
	std::vector<std::string> exports;

	void force_tabs     (std::string source);
	void handle_if      (std::string source);
	void handle_func    (std::string source);
	void handle_while   (std::string source);
	void handle_switch  (std::string source);
	void handle_enum    (std::string source);
	void handle_struct  (std::string source);
	void handle_var     (std::string source);
	void remove_comments(std::string source);
}

void compile_source(std::string source);
bool compile_header(std::string source);

#endif
