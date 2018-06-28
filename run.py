<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-



from app import app
app.run(debug=True)
=======
from app import app
app.run(debug=True, threaded=True, host="0.0.0.0")
>>>>>>> 2a7ff4b1c703d4905ad846630aeab3621467d0fa
