import { TestBed, inject } from '@angular/core/testing';

import { RolelistService } from './rolelist.service';

describe('RolelistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [RolelistService]
    });
  });

  it('should be created', inject([RolelistService], (service: RolelistService) => {
    expect(service).toBeTruthy();
  }));
});
