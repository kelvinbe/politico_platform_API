from ....database_config import init_db


class BaseModel(object):
    def check_if_item_exists(self, table_name, field_name, value):
        connect = init_db()
        cur = connect.cursor()
        query = "SELECT * FROM {} WHERE {}='{}';".format(table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchall()
        if resp:
            return True
        else:
            return False


    def delete_it(self, table_name, field_name, value):
        if self.check_if_item_exists(table_name, field_name, value) == False:
            return "No such item"
        connect = init_db()
        cur = connect.cursor()
        query = "DELETE * FROM {} WHERE {}={};".format(table_name, field_name, value)
        cur.execute(query)
        connect.commit()
        cur.close()
        return 200

    def update_item(self, table_name, field_name, data, item_pri, item_id):

        if self.check_if_item_exists(table_name, item_pri, item_id) == False:
            return "No such item"

        connect = init_db()
        cur = connect.cursor()
        query = "UPDATE * SET {}='{}' \
             WHERE {}='{}';".format(table_name, field_name, item_pri, item_id)
        cur.execute(query)
        connect.commit()
        return 200
