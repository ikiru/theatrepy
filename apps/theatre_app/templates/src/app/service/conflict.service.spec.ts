import { TestBed, inject } from '@angular/core/testing';

import { ConflictService } from './conflict.service';

describe('ConflictService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ConflictService]
    });
  });

  it('should be created', inject([ConflictService], (service: ConflictService) => {
    expect(service).toBeTruthy();
  }));
});
