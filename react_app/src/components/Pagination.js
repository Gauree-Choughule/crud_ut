import React, { useState } from 'react';
import { Pagination } from 'react-bootstrap';

const PaginationComponent = ({ itemsPerPage, totalItems, paginate }) => {
  const pageNumbers = [];
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  for (let i = 1; i <= totalPages; i++) {
    pageNumbers.push(i);
  }

  const [activePage, setActivePage] = useState(1);

  const handlePageClick = (pageNumber) => {
    setActivePage(pageNumber);
    paginate(pageNumber);
  };

  return (
    <Pagination>
      {pageNumbers.map((number) => (
        <Pagination.Item
          key={number}
          active={number === activePage}
          onClick={() => handlePageClick(number)}
        >
          {number}
        </Pagination.Item>
      ))}
    </Pagination>
  );
};

export default PaginationComponent;