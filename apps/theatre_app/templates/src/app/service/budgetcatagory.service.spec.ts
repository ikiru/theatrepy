import { TestBed, inject } from '@angular/core/testing';

import { BudgetcatagoryService } from './budgetcatagory.service';

describe('BudgetcatagoryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BudgetcatagoryService]
    });
  });

  it('should be created', inject([BudgetcatagoryService], (service: BudgetcatagoryService) => {
    expect(service).toBeTruthy();
  }));
});
