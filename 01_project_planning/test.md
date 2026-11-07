# Phase 3: HTML Structure — Expense Tracker

## Essential Topics and Project Tasks

| Order | Required Topics | Project Component / Kyun Chahiye | Prerequisite | Project Implementation Task |
| --- | --- | --- | --- | --- |
| 1 | Elements, opening/closing tags, nesting, basic attributes | Page ka introductory content likhna | Koi HTML knowledge required nahi | “Expense Tracker” heading aur introduction banayein. Ek paragraph mein `Total: 0 PKR` dikhayein; amount ko `<strong>` mein rakhein aur paragraph ko `expense-total` ID dein. |
| 2 | Document skeleton: `doctype`, `html`, `head`, `body`, `title`, charset, viewport | Proper project page banana | Block 1 | `index.html` banayein. Required document structure likhein, browser-tab title set karein, aur Block 1 ka content `<body>` mein place karein. |
| 3 | Heading hierarchy, `header`, `main`, `section`, basic `id`/`class` | Page ko clear project sections mein organize karna | Block 2 | Existing page ko organize karein: introduction ke liye header, aur main content mein “Add Expense,” “Expense History,” aur “Summary” sections banayein. Har section ko heading aur unique ID dein. |
| 4 | `form`, `label`, text/number `input`, `id`, `for`, `name`, submit `button` | Expense entry form ki foundation | Block 3 | “Add Expense” section mein expense name aur amount ke labelled fields banayein. Har label ko uske input se connect karein, inputs ko names dein, aur “Add Expense” submit button add karein. |
| 5 | `select`, `option`, `required`, `min`, `step`; basic submission concepts | Category selection aur form constraints | Block 4 | Form mein Food, Travel, Shopping aur Bills dropdown add karein. Required fields set karein. Amount ke liye minimum `0.01` aur decimal step `0.01` rakhein. Empty submission aur invalid amount se browser behavior test karein. |
| 6 | `table`, `caption`, `thead`, `tbody`, `tr`, `th`, `td`, `scope` | Expense records aur category totals dikhana | Blocks 3–5 | “Expense History” mein name, category aur amount ki table banayein; 3 sample records add karein. “Summary” mein category-wise totals ki table aur overall total dikhayein. Sample figures aapas mein consistent rakhein. |
| 7 | Integration, HTML structure review, label/heading checks, keyboard testing | Complete static Expense Tracker page | Blocks 1–6 | Puri page review karein: sections ka order, unique IDs, connected labels, table headings aur sample totals check karein. Keyboard se form use karein aur browser validation test karein. |

## Optional Advanced Topics

| Optional Topic | Project Implementation Task — Sirf Zaroorat Par |
| --- | --- |
| Links aur `nav` | Page ke sections tak jaane ke liye navigation links banana |
| `fieldset` aur `legend` | Form ke related fields ko labelled groups mein organize karna |
| `details` aur `summary` | Expandable “How to use this tracker” instructions banana |

# Python Topic Roadmap — Expense Tracker

## Essential Learning Blocks

| \# | Learning Block | Topics | Project Component | Prerequisite | Project Implementation Task |
| --- | --- | --- | --- | --- | --- |
| 1 | Python basics | Variables, data types, `input()`, `print()`, arithmetic | Expense amount, category, total calculation | None | User se expense name, category, amount aur monthly budget lein. Expense details aur expense ke baad remaining budget print karein. |
| 2 | Decisions | Comparison operators, `if`, `elif`, `else`, Boolean logic | Validate amount, category, budget alerts | Block 1 | `expense_validation.py` mein amount zero ya negative hone, category khaali/invalid hone aur amount budget se zyada hone ke cases handle karein. Har case ka suitable message dikhayein. |
| 3 | Repeating work | `while` loop, `for` loop, `range()` | Add multiple expenses, process transaction list | Block 1 | `expense_repetition.py` mein user ko multiple expenses enter karne dein. Quit option rakhein, invalid expenses skip karein, aur end mein valid expenses ka count, total aur remaining budget dikhayein. |
| 4 | Collections | Lists, tuples, dictionaries, nested data | Store transactions, categories, monthly summaries | Blocks 1–3 | Har expense ko dictionary aur saare expenses ko list mein store karein. Allowed categories ke liye tuple use karein. `category_summary.py` mein category-wise totals ki dictionary banayein aur summary print karein. |
| 5 | Reusable logic | Functions, parameters, return values, scope | Calculate totals, validate forms, generate reports | Blocks 1–4 | `expense_functions.py` mein amount/category validation, expense add karne, total calculate karne aur category summary banane ke functions likhein. Valid expense hi save ho; functions ko valid aur invalid inputs se test karein. |
| 6 | Error handling | `try`, `except`, `finally`, custom messages | Handle invalid amount, missing category, file errors | Blocks 1–5 | Amount mein text enter hone par program crash na hone dein; clear message ke baad dobara input lein. Missing category ko validation se handle karein. Block 8 mein file operations add hone ke baad file-error handling extend karein. |
| 7 | Strings & dates | String methods, f-strings, `datetime`, date formatting | Expense notes, monthly filters, report dates | Blocks 1–5 | Expense names, categories aur notes clean karein. Har expense mein date add karein, invalid date handle karein, selected month ke expenses filter karein aur formatted monthly report print karein. |
| 8 | Files | Reading/writing text and CSV files | CSV import/export and backup | Blocks 4–6 | Expenses ko CSV mein save aur program restart par load karein. Amount/date ko suitable types mein convert karein. Missing file ya invalid rows handle karein aur text summary backup banayein. |
| 9 | Modules & packages | `import`, standard modules, virtual environment, `pip` | Organize Flask app, use Flask/SQLAlchemy/pandas | Blocks 1–8 | Existing code ko validation, expense operations, summaries aur file storage modules mein organize karein. Main entry file se functions import karein. Virtual environment aur dependency list banayein; packages relevant later blocks mein add karein. |
| 10 | OOP basics | Classes, objects, attributes, methods | Transaction, Category, Budget models | Blocks 4–6 | `Transaction`, `Category` aur `Budget` ki simple classes banayein. Sample objects create karke transaction details, category information aur budget remaining calculate/display karne wale methods test karein. |
| 11 | Database logic | SQL basics, SQLite, SQLAlchemy queries | Save/load transactions, budgets, categories | Blocks 5, 9, 10 | Categories, transactions aur budgets ke database tables/models banayein. Records add, read, update aur delete karein. CSV storage ke bajaye database se records load karein aur monthly/category queries test karein. |
| 12 | Flask essentials | Routes, request/response, templates, forms, sessions | Web pages, Add Expense form, dashboard | Blocks 5–11 | Existing HTML pages ko Flask templates se connect karein. Expense list/dashboard routes aur Add Expense form submission implement karein. Server-side validation ke baad database mein save karein, success/error feedback dein aur session mein selected report month jaisi preference rakhein. |
| 13 | Data analysis | pandas basics: DataFrame, filtering, grouping, aggregation | Monthly totals, category breakdown, reports | Blocks 4–8 | CSV data se DataFrame banayein. Dates/amounts prepare karein, selected month filter karein, category-wise totals aur monthly totals calculate karein aur report CSV export karein. Database integration ke baad wahi analysis database records par apply karein. |
| 14 | Visualization | Matplotlib basics: pie, bar, line charts | Analytics dashboard and PDF charts | Block 13 | Category spending ka bar/pie chart aur monthly spending trend ka line chart banayein. Clear titles, labels aur units dein; empty data handle karein. Charts ko images ke taur par save karein aur PDF report mein use karne ke liye prepare karein. |
| 15 | Testing | pytest basics, test functions, assertions | Test calculations, validation and routes | Blocks 5–12 | Validation, expense saving, totals aur category summaries ke automated tests likhein. Zero/negative amounts, invalid categories aur empty data test karein. Flask routes aur valid/invalid form submissions ke tests add karein. |

## Optional Advanced Block

| \# | Learning Block | Topics | Project Component | Prerequisite | Project Implementation Task |
| --- | --- | --- | --- | --- | --- |
| 16 | Advanced optional | Decorators, generators, regex, type hints | Advanced validation, rules engine, clean code | Block 12; relevant earlier blocks | Existing functions mein type hints add karein. Sirf actual need par regex-based text rules, large CSV processing ke liye generator, ya repeated route behavior ke liye decorator implement karein. Har addition ko tests se verify karein. |

## Implementation Rules

1. Har block pehle seekhein, phir uska project task solve karein.
2. Existing project code ko extend/refactor karein; har baar project dobara start na karein.
3. Har task ke normal, invalid aur boundary test cases check karein.
4. Review aur corrections ke baad next block par move karein.
5. Block 9 mein pehle se bani files ko modules ke taur par organize/connect karein.
6. Flask block ke liye HTML form/page structure ka basic knowledge bhi required hoga.
7. Charts banana aur complete PDF document generate karna alag tasks hain; PDF generation ka tool relevant reporting stage par separately cover karein.
8. Optional advanced topics sirf project ki actual need par implement karein.

# Phase 4: CSS Design — Expense Tracker

## Essential Topics and Project Implementation Tasks

| Order | Required Topics | Project Component / Kyun Required Hai | Prerequisite | Project Implementation Task |
| --- | --- | --- | --- | --- |
| 1 | CSS rule syntax; external stylesheet; element selector | HTML page ko styling se connect karna | Basic HTML document | Existing project page ko `styles.css` se connect karein. Main heading ka color aur page ka background set karein. |
| 2 | Class selectors, basic descendant selectors; cascade, inheritance, specificity | Reusable styling aur conflicting rules samajhna | Block 1; HTML classes | Summary cards ko shared class dein. Sab cards ka common style aur total amount ka separate style banayein. Browser inspector mein applied rules check karein. |
| 3 | Colors, fonts, `font-size`, `font-weight`, `line-height`; `px`, `rem`, `%` | Headings, amounts aur messages readable banana | Block 2 | Page ka base font, heading sizes, readable text spacing aur consistent color palette set karein. Error/success message mein color ke saath clear text bhi rakhein. |
| 4 | Box model: margin, padding, border, `box-sizing`; width, `max-width`; normal flow and basic `display` | Page container aur sections ki spacing | Block 3 | Main content ko limited-width centered container mein rakhein. Form, summary aur history sections mein consistent padding, gaps aur borders add karein. |
| 5 | Form styling; `:hover`, `:focus-visible`, `:disabled`; table styling | Usable expense form aur readable expense history | Block 4; HTML forms/tables | Labels, inputs, dropdown aur button style karein. Visible keyboard focus dein. Table headers, cell padding aur amount alignment improve karein. |
| 6 | Flexbox: container/items, direction, gap, wrapping, alignment | Summary cards aur action buttons arrange karna | Block 4 | Summary cards ko flexible row mein arrange karein; space kam ho to wrap hon. Related action buttons align karein. |
| 7 | Mobile-first layout, media queries, flexible sizing, overflow | Small screens par usable tracker | Blocks 5–6 | Mobile par sections stack karein; wider screens par suitable arrangement dein. Expense table ko wrapper ke andar horizontally scrollable banayein, poori page ko nahi. |
| 8 | Browser DevTools review; responsive and accessibility checks | Complete design ki final checking | Blocks 1–7 | Narrow/wide screens, long expense names, empty table, error messages aur keyboard navigation test karein. Overflow, spacing aur conflicting rules fix karein. |

## Optional Advanced Topics

| Topic | Kab Project Mein Use Karenge? | Optional Project Task |
| --- | --- | --- |
| CSS Grid | Dashboard ko more structured rows/columns chahiye hon | Form aur summary ko desktop dashboard grid mein arrange karein. |
| CSS custom properties | Repeated colors/spacing centrally manage karni ho | Shared color aur spacing variables banayein. |
| Print styles | Browser se clean report print karni ho | Print mein form/buttons hide karke summary/table format karein. |

# Phase 5: Flask Basics — Expense Tracker

## Phase Goal

Existing HTML/CSS interface ko Python expense logic se connect karna:

- Dashboard aur expense history browser mein dikhana.
- Form se expense receive aur validate karna.
- Valid expense ko existing storage layer mein save karna.
- Totals, category summaries aur useful feedback dikhana.

## Prerequisites

- Python functions, parameters, return values, lists and dictionaries.
- Imports, modules and basic error handling.
- Basic HTML forms: label, input, select, name, method and button.
- Existing HTML/CSS page structure.
- Database knowledge sirf database integration task ke liye required hai.

## Essential Topics and Project Implementation Tasks

| Order | Learning Block / Required Topics | Project Component / Kyun Required Hai | Prerequisite | Project Implementation Task |
| --- | --- | --- | --- | --- |
| 1 | Setup: virtual environment, Flask installation, minimal app, local development server | Project ko browser se run karna | Python basics, imports; terminal basics | Existing project mein Flask entry file `app.py` banayein. Minimal application run karein aur browser par “Expense Tracker” response dikhayein. Development server ko sirf local practice ke liye use karein. |
| 2 | Request-response basics; routes, view functions, GET, endpoints, `url_for()` | Dashboard aur expense-history URLs define karna | Block 1; Python functions | Dashboard aur expense-history ke GET routes banayein. Har route filhaal simple response de. URL generation aur navigation ka connection samjhein. |
| 3 | `templates/`, `static/`, `render_template()`; Jinja variables, loops and conditions | Existing HTML/CSS ko dynamic expense data se connect karna | Block 2; HTML/CSS, lists and dictionaries | HTML ko templates folder aur CSS ko static folder mein organize karein. Sample expenses Python se template ko pass karein. Table rows, totals aur “No expenses yet” message dynamically render karein. |
| 4 | Jinja template inheritance: `base.html`, `extends`, `block`; shared navigation | Pages mein same layout aur styling reuse karna | Block 3 | Shared header, navigation aur stylesheet link ko `base.html` mein rakhein. Dashboard, history aur Add Expense pages ko us layout se extend karein. |
| 5 | Form submission: GET vs POST, form `action`, `request.form`; conversion and server-side validation | Browser form ko existing Python validation logic se connect karna | Block 4; Python validation and error handling | Add Expense form ke GET/POST flow banayein. Amount, category, name aur date receive karein. Existing validation functions reuse karein. Invalid input par error aur entered values dobara dikhayein; invalid expense save na ho. |
| 6 | Storage integration; separation of routes, business logic and persistence | Valid expense save karna aur updated records load karna | Block 5; existing file/database storage functions | Validated expense ko existing storage function se save karein. Dashboard aur history ke liye records aur summaries load karein. Database ready ho to existing database layer use karein; warna temporary CSV-backed storage use karein. |
| 7 | `redirect()`, Post/Redirect/Get, `flash()`; session basics for feedback, secret-key configuration; CSRF protection | Successful submission ka clean flow aur safer state-changing forms | Blocks 5–6 | Save ke baad success message flash karke history/dashboard par redirect karein. Refresh par normal form resubmission avoid karein. Secret key securely configure karein aur Flask-WTF CSRF protection add karein. |
| 8 | GET query parameters, `request.args`; optional filter defaults and validation | Monthly/category filtering aur filtered summaries | Blocks 6–7; date/filtering functions | Month aur category filter form banayein. Query parameters validate karke matching expenses, total aur category summary dikhayein. No-match case handle karein. |
| 9 | Error pages, basic logging and Flask test client | Complete web flow verify karna aur useful failures dikhana | Blocks 1–8; pytest basics if automated tests use karein | Friendly 404/500 pages add karein. Empty data, valid submission, invalid amount/category, save failure aur filters test karein. Check karein ke invalid submission storage change nahi karti aur successful POST redirect karta hai. |

## Optional / Later Topics

| Topic | Kab Required Hoga? | Project Implementation Task |
| --- | --- | --- |
| Dynamic routes and edit/delete flows | Expense editing/deletion add karni ho | Expense ID se edit form load karein. Update/delete ko CSRF-protected POST requests se handle karein; missing ID par 404 return karein. |
| Blueprints and application factory | Routes/configuration badhne lage | Dashboard, expenses aur reports ko separate modules/blueprints mein organize karein. |
| User authentication and ownership checks | Multiple users ke private expense accounts chahiye hon | Login/logout add karein aur har record par current user ki ownership enforce karein. Multi-user release se pehle yeh required hoga. |
| CSV download response | Browser se report export chahiye ho | Filtered expense data ki downloadable CSV response banayein. |
| JSON responses | Later JavaScript-based interactions chahiye hon | Required expense/summary endpoint se structured JSON return karein. |

## Scope Boundaries

- Is phase mein Python validation logic dobara nahi likhenge; existing functions reuse/refactor karenge.
- Jinja ka required subset hi seekhenge, complete template-language syllabus nahi.
- Sessions ko expense database ke replacement ke taur par use nahi karenge.
- Browser validation ke saath server-side validation bhi rakhenge.
- Production deployment is phase ka part nahi; public release se pehle separate deployment/security work required hoga.

## Learning and Implementation Flow

1. Sirf current block seekhein.
2. Us block ka project task existing project mein implement karein.
3. Code aur browser behavior review karein.
4. Corrections aur tests complete karein.
5. Phir next block par move karein.

# Phase 6: SQLite Database — Expense Tracker

## Phase Goal

Expense Tracker ke transactions, categories aur monthly budgets ko permanently store karna aur existing Flask pages ko database-backed banana.

## Prerequisites

- Python functions, lists, dictionaries and imports.
- Basic error handling and date handling.
- Flask routes, form processing and server-side validation.
- Existing expense validation and summary functions.
- SQL ka previous knowledge required nahi; required SQL isi phase mein seekhenge.

## Implementation Approach

- Pehle SQL aur Python ke built-in `sqlite3` module se database fundamentals implement karenge.
- SQLAlchemy ko isi phase mein parallel implement nahi karenge.
- Existing validation functions reuse karenge.
- Flask routes mein SQL scatter karne ke bajaye database operations ko separate functions/module mein rakhenge.
- Database integration ke baad CSV optional import/export rahega, primary storage nahi.

## Essential Topics and Project Implementation Tasks

| Order | Learning Block / Required Topics | Project Component / Kyun Required Hai | Prerequisite | Project Implementation Task |
|---|---|---|---|---|
| 1 | Database, table, row, column, primary key; SQLite database file; Python connection basics | Existing expense records ko persistent storage mein rakhna | Python functions and imports | Database responsibilities ke liye `database.py` module banayein. Configured project path par database connection open/close karne ka function likhein. Database file aur CSV file ka role distinguish karein. |
| 2 | Schema design; `CREATE TABLE IF NOT EXISTS`; `INTEGER`, `TEXT`; `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`; foreign keys | Transactions, categories aur budgets ka reliable structure | Block 1 | `categories`, `expenses` aur `budgets` tables design/create karein. Expense mein name, amount, date aur category reference rakhein. Monthly budget ke month ko unique rakhein. Foreign-key enforcement har connection par enable karein. |
| 3 | Money/date representation; `INSERT`, parameter placeholders; commit and rollback basics | Expense aur budget values accurately aur safely save karna | Block 2; Python validation/date handling | Money ko integer minor units mein store karein, jaise PKR paisa. Dates ko consistent `YYYY-MM-DD` text mein rakhein. Allowed categories insert karein aur validated expense/budget save karne ke parameterized functions banayein. |
| 4 | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`; fetching rows and named-column access | Expense history aur individual records load karna | Block 3 | Latest expenses date aur ID ke descending order mein load karein. ID se ek expense retrieve karein. Category aur date-range filters add karein; missing record aur empty results handle karein. |
| 5 | `UPDATE`, `DELETE`, targeted `WHERE`; row counts | Expense correction aur removal | Block 4 | Expense ID se update/delete functions likhein. Update se pehle input validate karein. Missing ID ka clear result dein aur confirm karein ke sirf intended record change hota hai. |
| 6 | `JOIN`, `SUM`, `COUNT`, `GROUP BY`, `COALESCE`; monthly date ranges | Dashboard totals, category summary aur remaining budget | Block 4 | Expense rows ke saath category names retrieve karein. Selected month ka total, expense count aur category-wise totals calculate karein. No-expense case mein total zero dein. Monthly budget aur spending se remaining amount calculate karein. |
| 7 | Transactions, constraint errors, rollback and connection cleanup | Failed writes se partial/inconsistent changes avoid karna | Blocks 3–6; Python error handling | Related multi-step writes ko ek transaction mein rakhein. Duplicate category, invalid category reference aur failed save test karein. Failure par rollback aur har outcome mein connection cleanup ensure karein. |
| 8 | Flask integration; request-scoped connections and teardown; storage-function boundaries | Existing web interface ko database se connect karna | Blocks 1–7; Flask forms/routes | Flask ke Add Expense, history aur dashboard flows ko database functions se connect karein. Successful save ke baad redirect karein. Page reload aur app restart ke baad records verify karein. GET requests se records change na karein. |
| 9 | Temporary test databases; persistence checks; basic backup/restore | Database implementation verify aur project data protect karna | Blocks 1–8 | Real project data se separate test database use karein. Valid/invalid writes, filters, totals, updates, deletes aur rollback test karein. Database backup banayein aur separate copy se restore/load verify karein. |

## Minimum Data Model

| Table | Required Data | Project Purpose |
|---|---|---|
| `categories` | ID, unique category name | Allowed expense categories |
| `expenses` | ID, expense name, amount in minor units, expense date, category ID | Individual expense records |
| `budgets` | ID, unique month in `YYYY-MM` format, budget amount in minor units | Monthly budget comparison |

## Optional / Later Topics

| Topic | Kab Required Hoga? | Project Implementation Task |
|---|---|---|
| Indexes and `EXPLAIN QUERY PLAN` | Records badhne par filters noticeably slow hon | Actual date/category queries inspect karein aur useful indexes add karke compare karein. |
| CSV import | Existing CSV expenses migrate karne hon | Rows validate karein, invalid rows report karein aur accidental repeat imports handle karein. |
| Schema migrations | Saved data ko preserve karte hue table structure change karna ho | Versioned migration se required column/table add karein; pehle backup aur migration test karein. |
| SQLAlchemy integration | Later project architecture ORM use kare | Existing schema aur operations ko models/queries mein map karein; duplicate raw-SQL/ORM storage paths avoid karein. |
| User ownership | Multiple users ke private records chahiye hon | User references aur ownership-scoped queries add karein. Multi-user release se pehle authentication/authorization integration required hoga. |

## Important Project Rules

1. User input ko SQL strings mein f-strings ya concatenation se insert na karein; value placeholders use karein.
2. Browser validation ke saath Python validation aur database constraints bhi rakhein.
3. Category delete karne ki policy explicitly choose karein; existing expenses ko accidentally delete na hone dein.
4. Money calculations ke liye binary float se direct storage conversion avoid karein; decimal input ko carefully minor units mein convert karein.
5. Monthly filters ke liye start-of-month inclusive aur next-month-start exclusive date range use karein.
6. Table initialization existing saved records ko delete/reset na kare.
7. Project ke expense records ko browser session ya global list mein permanent storage ke taur par na rakhein.
8. Har block ke baad uska project task implement aur review karein; phir next block par move karein.