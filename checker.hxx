/*
 * checker.hxx
 *
 * (C) EN 2025 - THIS CODE IS UNDER THE MIT LICENSE
 *
 * created for the mutt programming language
 */

#include<iostream>

#ifndef MUTT_CHECKER_H
#define MUTT_CHECKER_H

bool check_brackets  (std::string source);
bool check_indents   (std::string source);
bool check_statements(std::string source);
bool check_symbols   (std::string source);
bool check_syntax    (std::string source);

#endif
