from create_db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    as_executor_in_offers = db.relationship('Offer', foreign_keys='Offer.executor_id')  # Положит список всех оферов
    # в которых он указан как исполнитель
    as_executor_in_orders = db.relationship('Order', foreign_keys='Order.executor_id')
    as_customer_in_orders = db.relationship('Order', foreign_keys='Order.customer_id')

    def to_dict(self):
        return {
            'id:': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email,
            'role': self.role,
            'phone': self.phone
        }


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    start_date = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    address = db.Column(db.String(255))
    price = db.Column(db.Integer)

    customer_id = db.Column(db.Integer, db.ForeignKey(User.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))

    as_order_in_offers = db.relationship('Offer')  # Ищет в Офере внешний ключ ссылающийся

    # на него самого и кладет в переменную

    def to_dict(self):
        return {
            'id:': self.id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'address': self.address,
            'price': self.price,
        }


class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))

    order = db.relationship('Order', back_populates="as_order_in_offers", foreign_keys=[order_id])  # кладет экз. заказа
    # на который ссылается внешний ключ
    # order_id(as_order_in_offers)
    executor = db.relationship('User', back_populates="as_executor_in_offers", foreign_keys=[executor_id])  #

    def to_dict(self):
        return {
            'id:': self.id,
            'order_id': self.order_id,
            'executor_id': self.executor_id
        }



db.create_all()