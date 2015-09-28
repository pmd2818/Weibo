#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# github:https://github.com/tangthis
# user ORM对象模型

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

#创建User类
#字段使用db.Column类创建实例
#__repr__方法告诉Python如何打印class对象，方便我们调试使用。 
class User(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	nickname = db.Column(db.String(64),index = True ,unique = True)
	email = db.Column(db.String(120),index = True,unique = True)
	role = db.Column(db.SmallInteger,default = ROLE_USER)
	posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
	
	def __repr__(self):
		return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 
    def __repr__(self):
        return '<Post %r>' % (self.body)