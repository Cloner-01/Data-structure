فرمت‌های عبارات 📚                                                                                                                                                       
                                                                                                                                                                                 Infix 🎯
                                                                                                                                                                                 
فرمت معمولی که در ریاضیات استفاده می‌شود.

مثال: A + B
                                                                                                                                                          Postfix (نشانه‌گذاری معکوس لهستانی) 🔄
عملگر بعد از عملوندها می‌آید.

مثال: + A B 
                                                                                                                                                                 Prefix (نشانه‌گذاری لهستانی) 🔄
عملگر قبل از عملوندها می‌آید.

مثال: A B +

تبدیل بین تمامی حالات 🔄
1. تبدیل Infix به Postfix 📥 → 📤
الگوریتم: از پشته (Stack) برای مدیریت عملگرها و پرانتزها استفاده می‌شود.

مثال:

ورودی: A + B * C

خروجی: + * A B C

2. تبدیل Infix به Prefix 📥 → 🔝
الگوریتم: عبارت Infix را برعکس کنید، سپس به Postfix تبدیل کرده و دوباره برعکس کنید.

مثال:

ورودی: A + B * C

خروجی: A * B C +

3. تبدیل Postfix به Infix 📤 → 📥
الگوریتم: از پشته برای تبدیل عملگرها و عملوندها به فرمت Infix استفاده می‌شود.

مثال:

ورودی: + * A B C

خروجی: A + B * C

4. تبدیل Prefix به Infix 🔝 → 📥
الگوریتم: عبارت Prefix را برعکس کنید، سپس به Postfix تبدیل کرده و دوباره برعکس کنید.

مثال:

ورودی:  A * B C +

خروجی: A + B * C

5. تبدیل Postfix به Prefix 📤 → 🔝
الگوریتم: ابتدا Postfix را به Infix تبدیل کنید، سپس Infix را به Prefix تبدیل کنید.

مثال:

ورودی: + * A B C

خروجی:  A * B C +

6. تبدیل Prefix به Postfix 🔝 → 📤
الگوریتم: ابتدا Prefix را به Infix تبدیل کنید، سپس Infix را به Postfix تبدیل کنید.

مثال:

ورودی:  A * B C +

خروجی: + * A B C 

مثال‌های کامل 📖

مثال 1: 
                                                                                             Infix: (A + B) * (C - D)     Postfix: A B + C D - *   Prefix: * + A B - C D
                                                                                                                                                              
مثال 2:
                                                                                             Infix: A + B * C / D - E      Postfix: A B C * D / + E -   Prefix: - + A / * B C D E
                                                                                                                                                              
مثال3:         Infix: (A * B) + (C / D)        Postfix: A B * C D / +     Prefix: + * A B / C D            
                                                                                                 

نکات مهم ⚠️

از پرانتزها برای اولویت‌بندی عملیات استفاده کنید. 🎯

فاصله بین عملوندها و عملگرها رعایت شود. 📏

این ابزار برای عبارات ساده و بدون خطا طراحی شده است. 🛠️

شروع کار 🚀
برای استفاده از این ابزار، کافیست عبارت خود را وارد کرده و نوع تبدیل مورد نظر را انتخاب کنید. 🖥️

نکته: این ابزار برای یادگیری و درک بهتر مفاهیم تبدیل عبارات ریاضی طراحی شده است. 🎓
