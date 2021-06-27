# Printing Arrow Pattern
# minimize the number of print() function invocations by inserting the \n sequence into the strings

# method 1
print("       *\n", "     *  *\n", "   *      *\n", "  *        *\n", "* * *   * * *\n", "    *   *\n", "    *   *\n",
      "    *****", sep="")

# method 2
print(" " * 4, "*\n", " " * 2, "* *\n", " ", "*", " ", "*\n", "", "*", " " * 3, "*\n", "*" * 3, " ", "*" * 3, "\n",
      "  *   * \n " * 2, "", "*" * 5)

# method 3. Big arrow
print(" " * 12, "*\n", " " * 10, "*", " " * 3, "*\n", " " * 8, "*", " " * 7, "*\n", " " * 6, "*", " " * 11, "*\n",
      " " * 4, "* " * 3, " " * 6, "* " * 3, sep="")
print(" " * 8, "*", " " * 7, "*\n", " " * 8, "*", " " * 7, "*\n", " " * 8, "*", " " * 7, "*\n", " " * 8, "* " * 5, "\n",
      sep="")

# method 3. Big arrow. Filled with *
print(" " * 12, "*\n", " " * 10, "*", "*" * 3, "*\n", " " * 8, "*", "*" * 7, "*\n", " " * 6, "*", "*" * 11, "*\n",
      " " * 4, "*" * 17, sep="")
print(" " * 8, "*", "*" * 7, "*\n", " " * 8, "*", "*" * 7, "*\n", " " * 8, "*", "*" * 7, "*\n", " " * 8, "*" * 9, "\n",
      sep="")
