import React from 'react';

const DeleteConfirmationModal = ({ onCancel, onConfirm }) => (
  <div style={{ position: 'fixed', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', border: '1px solid black', padding: '20px', backgroundColor: 'white' }}>
    <p>Are you sure you want to delete this book?</p>
    <button onClick={onCancel} style={{ marginRight: '10px' }}>Cancel</button>
    <button onClick={onConfirm}>Delete</button>
  </div>
);

export default DeleteConfirmationModal;
