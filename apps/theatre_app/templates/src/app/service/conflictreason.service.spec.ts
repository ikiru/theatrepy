import { TestBed, inject } from '@angular/core/testing';

import { ConflictreasonService } from './conflictreason.service';

describe('ConflictreasonService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ConflictreasonService]
    });
  });

  it('should be created', inject([ConflictreasonService], (service: ConflictreasonService) => {
    expect(service).toBeTruthy();
  }));
});
