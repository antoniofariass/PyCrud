### :information_source: How To Use
  
To clone and run this application in your local machine, you'll need [Git](https://git-scm.com), [Python V3.9](https://www.python.org/downloads/) or higher + [Azure](https://azure.microsoft.com/pt-br/downloads/)
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/antoniofariass/PyCrud.git

$ venv\Scripts\Activate.ps1
$ .\venv\Scripts\pip3.exe install -r requirements.txt

$ func host start 

```

To run this application in your insonia with my code deployed in Azure, use the nexts endpoint: 

```bash
  
  create_user: https://pycrud.azurewebsites.net/api/create_user
        # Use the json body on request:
        {
        "id" : "",
        "name":"",
        "email": "",
        "age": ,
        "city": ""
        }
  
  delete_user: https://pycrud.azurewebsites.net/api/users/Put_the_id_here
                                                         
  read_user: https://pycrud.azurewebsites.net/api/users/Put_"all"_to_read_all_or_"unique"_to_Read_unique_id/Put_the_id_to_read_unique_or_"00"_to_read_all
  
  update_user: https://pycrud.azurewebsites.net/api/users/the
      # Use this json body on request: 
      {
      "name":"Marcelo",
      "age": 40,
      "city": "São Jose dos Campos"
      }
```
