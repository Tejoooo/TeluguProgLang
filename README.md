# 📜 TeluguLang – A Simple Programming Language in Telugu

**TeluguLang** is a custom-made interpreted language that allows you to write code using Telugu keywords — either in native Telugu script or transliterated English. It includes support for variables, loops, conditionals, and user-defined functions.

---

## 🚀 Features

- ✅ Variable declarations with `విలువ` / `viluva`
- ✅ Print using `రాయీ` / `raayi`
- ✅ Arithmetic and expressions
- ✅ For and While loops
- ✅ Custom function support with return
- ✅ Full Unicode (Telugu) support
- ✅ Both Telugu script and Roman Telugu supported

---

## 📦 Project Structure

```
telugu_lang/
├── ast_nodes.py         # AST structure
├── interpreter.py       # Evaluator/interpreter
├── lexer.py             # Tokenizer
├── parser.py            # Parser for syntax
├── main.py              # Entry point
├── sample.tl            # Sample TeluguLang program
├── run.sh               # Shell script to execute
└── README.md            # This file
```

---

## ⚙️ How to Run

1. **Clone the repo**
   ```bash
   
   git clone https://github.com/Tejoooo/TeluguProgLang.git
   cd TeluguProgLang
   ```

2. **Make the shell script executable**
   ```bash
   chmod +x run.sh
   ```

3. **Run the interpreter**
   ```bash
   ./run.sh
   ```

   ✅ Output will be shown for the file `sample.tl`.

---

## 🧪 Example Program (`sample.tl`)

```tl
మొదలు

విలువ x = 0;
విలువ j = 0;
విలువ s = "Hello World";
విలువ d = 0;
విలువ g = 0;
విలువ p = 0;

రాయీ s;

// For Loop
కోసం i = 1 to 5 లోపల    
    విలువ g = g + i;       
ఆపే
రాయీ "ForLoopValue " + g;

// While Loop
విలువ m = 0;
లూప్ m <= 5 లోపల
    విలువ p = p + 1;
    m = m + 1;
ఆపే
రాయీ "WhileLoopValue " + p;

// Function to add two numbers
సృష్టించు add(x, y)
లోపల
    విలువ result = x + y;
    పంపించు result;
ఆపే

// Function to subtract two numbers
సృష్టించు sub(x, y)
లోపల
    విలువ d = x - y;
    పంపించు d;
ఆపే

ans = add(10, 20);
d = sub(23, 4);

రాయీ "Addition value " + ans;
రాయీ "Subtraction value " + d;

ముగింపు
```

---

## 🔑 Keyword Reference

| Telugu       | English (Transliterated) | Meaning               |
|--------------|---------------------------|------------------------|
| మొదలు        | modalu                    | Start of program       |
| ముగింపు      | mugimpu                   | End of program         |
| విలువ        | viluva                    | Variable declaration   |
| రాయీ         | raayi                     | Print statement        |
| కోసం         | kosam                     | For loop               |
| లోపల         | lopala                    | Inside loop/function   |
| లూప్         | loopu                     | While loop             |
| ఆపే         | aape                      | End of loop/function   |
| సృష్టించు     | srishtinchu               | Function definition    |
| పంపించు       | pampinchu                 | Return value from func |

---

## 💡 Notes

- Both Telugu and Roman Telugu are supported for writing programs.
- Variable names and strings can be in English or Telugu.
- Spaces, indentation, and semicolons (`;`) are important in parsing.

---

## 🌱 Future Scope

- 🌐 **Web IDE**: An online editor with Telugu script support and live code execution.
- 🧪 **Unit Testing**: Support for defining and running tests in TeluguLang.
- 📦 **Package Support**: Ability to import libraries written in TeluguLang.
- 🎨 **GUI Applications**: Build basic GUI-based apps using TeluguLang syntax.
- 🗣️ **Voice Code Input**: Convert spoken Telugu code into syntax automatically.
- 📚 **Docs & Tutorials**: Comprehensive documentation and interactive tutorials for beginners.
- 🚀 **Transpile to Python**: Compile TeluguLang code into native Python for better integration and deployment.

---

## 🙏 Contributions

Feel free to contribute by opening [issues](https://github.com/Tejoooo/TeluguProgLang/issues) or submitting [pull requests](https://github.com/Tejoooo/TeluguProgLang/pulls)!  
Let's bring coding to native language speakers! 🌍

---

## 🧑‍💻 Author

Made with ❤️ by Tejo Kaushal  
If you like the project, ⭐ it on GitHub!

---

## 📄 License

This project is licensed under the MIT License.

