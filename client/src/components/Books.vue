<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
<<<<<<< HEAD
        <h1>ToDos</h1>
=======
        <h1>Todos</h1>
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.todo-modal>Add Todo</button>
        <br><br>

<<<<<<< HEAD
        <!-- todos table -->
=======
        <!-- Todos table -->
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Todo</th>
              <th scope="col">Assignee</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(todo, index) in todos" :key="index">
<<<<<<< HEAD
              <td>{{ todo.todo }}</td>
              <td>{{ todo.assignee }}</td>
=======
              <td>{{ todo.title }}</td>
              <td>{{ todo.author }}</td>
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
              <td>
                <span v-if="todo.read">Yes</span>
                <span v-else>No</span>
              </td>
<<<<<<< HEAD
=======
              <td>${{ todo.price }}</td>
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.todo-update-modal
<<<<<<< HEAD
                        @click="editTodo(todo)">
=======
                        @click="edittodo(todo)">
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
                    Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
<<<<<<< HEAD
                        @click="onDeleteTodo(todo)">
=======
                        @click="onDeletetodo(todo)">
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
                    Delete
                </button>
                <router-link :to="`/order/${todo.id}`"
                             class="btn btn-primary btn-sm">
                    Purchase
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>

<<<<<<< HEAD
    <!-- add todo modal -->
    <b-modal ref="addTodoModal"
             id="todo-modal"
            todo="Add a new todo"
=======
    <!-- add Todo modal -->
    <b-modal ref="addTodoModal"
             id="todo-modal"
            title="Add a new Todo"
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-todo-group"
                      label="Todo:"
                      label-for="form-todo-input">
            <b-form-input id="form-todo-input"
                          type="text"
<<<<<<< HEAD
                          v-model="addTodoForm.todo"
=======
                          v-model="addTodoForm.title"
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
                          required
                          placeholder="Enter todo">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-assignee-group"
                      label="Assignee:"
                      label-for="form-assignee-input">
          <b-form-input id="form-assignee-input"
                        type="text"
<<<<<<< HEAD
                        v-model="addTodoForm.assignee"
                        required
                        placeholder="Enter assignee">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addTodoForm.done" id="form-checks">
              <b-form-checkbox value="true">Done?</b-form-checkbox>
=======
                        v-model="addTodoForm.author"
                        required
                        placeholder="Enter author">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-price-group"
                      label="Purchase price:"
                      label-for="form-price-input">
          <b-form-input id="form-price-input"
                        type="number"
                        v-model="addTodoForm.price"
                        required
                        placeholder="Enter price">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
            <b-form-checkbox-group v-model="addTodoForm.read" id="form-checks">
              <b-form-checkbox value="true">Read?</b-form-checkbox>
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
            </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

<<<<<<< HEAD
    <b-modal ref="editTodoModal"
             id="todo-update-modal"
             todo="Update"
=======
    <b-modal ref="edittodoModal"
             id="todo-update-modal"
             title="Update"
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-todo-edit-group"
                      label="Todo:"
                      label-for="form-todo-edit-input">
          <b-form-input id="form-todo-edit-input"
                        type="text"
                        v-model="editForm.todo"
                        required
                        placeholder="Enter todo">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-assignee-edit-group"
                      label="Assignee:"
                      label-for="form-assignee-edit-input">
          <b-form-input id="form-assignee-edit-input"
                        type="text"
                        v-model="editForm.assignee"
                        required
                        placeholder="Enter assignee">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      todos: [],
      addTodoForm: {
<<<<<<< HEAD
        todo: '',
        assignee: '',
        done: [],
=======
        title: '',
        author: '',
        read: [],
        price: '',
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
      },
      editForm: {
        id: '',
        todo: '',
        assignee: '',
        done: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTodos() {
      const path = 'http://localhost:5000/todos';
      axios.get(path)
        .then((res) => {
          this.todos = res.data.todos;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTodo(payload) {
      const path = 'http://localhost:5000/todos';
      axios.post(path, payload)
        .then(() => {
          this.getTodos();
<<<<<<< HEAD
          this.message = 'Todo added!';
=======
          this.message = 'todo added!';
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTodos();
        });
    },
    updateTodo(payload, todoID) {
      const path = `http://localhost:5000/todos/${todoID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTodos();
<<<<<<< HEAD
          this.message = 'Todo updated!';
=======
          this.message = 'todo updated!';
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTodos();
        });
    },
    removeTodo(todoID) {
      const path = `http://localhost:5000/todos/${todoID}`;
      axios.delete(path)
        .then(() => {
          this.getTodos();
<<<<<<< HEAD
          this.message = 'Todo removed!';
=======
          this.message = 'todo removed!';
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTodos();
        });
    },
    initForm() {
<<<<<<< HEAD
      this.addTodoForm.todo = '';
      this.addTodoForm.assignee = '';
      this.addTodoForm.done = [];
=======
      this.addtodoForm.title = '';
      this.addtodoForm.author = '';
      this.addtodoForm.read = [];
      this.addtodoForm.price = '';
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
      this.editForm.id = '';
      this.editForm.todo = '';
      this.editForm.assignee = '';
      this.editForm.done = [];
      this.editForm.id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
<<<<<<< HEAD
      let done = false;
      if (this.addTodoForm.done[0]) done = true;
      const payload = {
        todo: this.addTodoForm.todo,
        assignee: this.addTodoForm.assignee,
        done, // property shorthand
=======
      let read = false;
      if (this.addtodoForm.read[0]) read = true;
      const payload = {
        title: this.addtodoForm.title,
        author: this.addtodoForm.author,
        read, // property shorthand
        price: this.addtodoForm.price,
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
      };
      this.addTodo(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
<<<<<<< HEAD
      let done = false;
      if (this.editForm.done[0]) done = true;
=======
      let read = false;
      if (this.editForm.read[0]) read = true;
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
      const payload = {
        todo: this.editForm.todo,
        assignee: this.editForm.assignee,
        done, // property shorthand
      };
      this.updateTodo(payload, this.editForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTodoModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTodoModal.hide();
      this.initForm();
      this.getTodos(); // why?
    },
<<<<<<< HEAD
    onDeleteTodo(todo) {
      this.removeTodo(todo.id);
    },
    editTodo(todo) {
=======
    onDeletetodo(todo) {
      this.removeTodo(todo.id);
    },
    edittodo(todo) {
>>>>>>> 421539729d0491c42a99efbafe46c486408b15b6
      this.editForm = todo;
    },
  },
  created() {
    this.getTodos();
  },
};
</script>
