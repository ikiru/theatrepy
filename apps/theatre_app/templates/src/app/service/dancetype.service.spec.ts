import { TestBed, inject } from '@angular/core/testing';

import { DancetypeService } from './dancetype.service';

describe('DancetypeService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DancetypeService]
    });
  });

  it('should be created', inject([DancetypeService], (service: DancetypeService) => {
    expect(service).toBeTruthy();
  }));
});
