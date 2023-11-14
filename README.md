# AlloCamarade
The Efrei Project for create a REST API. The technology which will be used is Python/Flask

# Improvements notes
Improve front. 
- Currently really bad
- No detection of already logged in on login page
- Multiple requests done in many files but not centralized
- No variables used in CSS
- No Ajax used
- No Global URL used
- No SEO done at all
- CSS sucks

Improve Back.
- List Theaters is not available and not implemented
- No ORM used, only SQL requests on the top
- No MVC used for displaying result from database
- Add the Date Available feature processed on the Back and not on as currently on the front.

# Important notes (Back)
- JWT authentication working perfectly, with multiple handles for different use-case.
- Password treatment (SHA 256)
- Using a homemade "ORM-Styled" code, every launch the DB will be dropped, re-created and re-filled. This was really usefull during developpement.
- Using Object-based response, to add easily some logging (without logger, only colors-printed function), response code as enumeration etc.
- Handling bad responses reception, database errors, bad requests. 

All of that stuff was developped and merged in 2 to 3 hours, so don't be too much attentive to details...!
