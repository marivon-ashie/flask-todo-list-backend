from flask import Blueprint,jsonify,request
from flask_login import login_required
from app.models import Task
from app import db

task =Blueprint("task",__name__)




@task.route("/todos", methods=['POST'])
@login_required
def add_todo():
    try:
        data = request.get_json()
        new_todo = Task(title=data['title'])  
        db.session.add(new_todo)
        db.session.commit()
        
        # Call the helper method here
        return jsonify(new_todo.to_dict()), 201 
    except Exception as e:
        return jsonify({"Error": str(e)}), 400



@task.route("/todos", methods=['GET'])
@login_required
def get_task():
    task =Task.query.all()
    return jsonify([t.to_dict() for t in task]),201

    
    
        
@task.route('/todos/<int:id>',methods =['delete'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({"message":"Successfully Deleted"}),200


@task.route("/todos/<int:id>",methods=['put'])
@login_required
def update_task(id):
        task =Task.query.get_or_404(id)
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.is_completed=data.get('is_completed',task.is_completed)
        db.session.commit() 
        
        return jsonify(task.to_dict()),200




 
 
 
