# CS-340-10514-M01-Client-Server-Development

1) Writing Maintainable, Readable, and Adaptable Programs
When I built the CRUD Python module in Project One, I didn’t fully realize at first how important that separation would be in Project Two. Keeping all of the database operations in one file ended up saving me a lot of time. Instead of rewriting queries inside the dashboard code, I could just call the functions I had already tested.
I tried to keep the code readable by using straightforward function names and keeping each function focused on one responsibility (create, read, update, delete). That made debugging easier because if something broke, I knew exactly where to look.
The biggest advantage of working this way was flexibility. When I needed to adjust how data was filtered for the dashboard widgets, I didn’t have to redesign everything. I could modify the CRUD logic without touching the user interface code. In the future, I could reuse this same module structure for any application that connects to a database. I could also expand it by adding stronger validation or better error handling if this were a production system instead of a class project.

2) My Approach to Problem Solving as a Computer Scientist
For this project, I approached it more like a real client request instead of just completing an assignment. Grazioso Salvare had specific requirements for filtering and displaying rescue animal data, so I started by understanding what they needed the dashboard to actually do.
I broke the work into stages:
1.	Make sure the database connection worked properly.
2.	Confirm that CRUD operations returned the correct data.
3.	Connect those results to the dashboard filters and visualizations.
Compared to earlier courses, this felt more applied and layered. In previous classes, assignments were often isolated tasks. Here, everything depended on everything else working correctly. If the database query was wrong, the dashboard would display incorrect results.
In future projects, I would continue using this structured approach: analyze requirements first, design the database around how the data will be queried, test small pieces before combining them, and validate results before moving forward.

3) What Computer Scientists Do and Why It Matters
Computer scientists build systems that help organizations manage and use data more effectively. In this case, the dashboard allows a company like Grazioso Salvare to quickly filter animals by training type and see the results visually instead of manually searching through records.
Projects like this matter because they turn raw data into something usable. Instead of spending time sorting through spreadsheets or guessing, decision-makers can rely on structured tools. Even though this was a class project, it demonstrates how software can improve efficiency, accuracy, and overall workflow for a real organization.

