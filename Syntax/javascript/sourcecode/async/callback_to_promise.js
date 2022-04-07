'use strict';

class UserStorage {
  loginUser(id, password) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (
          (id === 'ellie' && password === 'dream') ||
          (id === 'coder' && password === 'academy')
        ) {
          resolve(id);
        } else {
          reject(new Error('not found'));
        }
      }, 2000);
    });
  }

  getRoles(user) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (user === 'ellie') {
          resolve({ name: 'ellie', role: 'admin' });
        } else {
          reject(new Error('no access'));
        }
      }, 1000);
   });
  }
}

const userStorage = new UserStorage();
const id = 'ellie' // prompt('enter your id');
const password = 'dream' // prompt('enter your passrod');

userStorage
  .loginUser(id, password)
  .then(userStorage.getRoles)
  .then((user) => console.log(`Hello ${user.name}, you have a ${user.role} role`))
  .catch(console.log);
